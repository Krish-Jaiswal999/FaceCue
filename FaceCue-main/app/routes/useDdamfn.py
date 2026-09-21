import os
import numpy as np
import cv2
import threading
import asyncio
import mediapipe as mp
from mediapipe.tasks import python as mp_python
from mediapipe.tasks.python import vision

from fastapi import APIRouter, File, UploadFile, HTTPException

from ddamfn.infer import DDAMFNPredictor

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root (this file lives in app/)
WEIGHTS_PATH = os.path.join(BASE_DIR, "ddamfn", "weights", "rafdb.pth")
LANDMARKER_PATH = os.path.join(BASE_DIR, "face_landmarker.task")

predictor = DDAMFNPredictor(WEIGHTS_PATH)

_base_options = mp_python.BaseOptions(model_asset_path=LANDMARKER_PATH)
_landmarker_options = vision.FaceLandmarkerOptions(base_options=_base_options, num_faces=1)
landmarker = vision.FaceLandmarker.create_from_options(_landmarker_options)
model_lock = threading.Lock()
MAX_UPLOAD_BYTES = 10 * 1024 * 1024

LANDMARK_IDX = {"left_eye": 33, "right_eye": 263, "nose": 1, "mouth_left": 61, "mouth_right": 291}


def get_5pt_landmarks(image_rgb: np.ndarray):
    h, w = image_rgb.shape[:2]
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
    result = landmarker.detect(mp_image)
    if not result.face_landmarks:
        return None
    lm = result.face_landmarks[0]
    pts = np.array([[lm[i].x * w, lm[i].y * h] for i in LANDMARK_IDX.values()], dtype=np.float32)
    return pts

@router.post("/post/image")
async def predict_emotion(image: UploadFile = File(...)):
    if not image.content_type or not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Uploaded file is not an image")

    raw_bytes = await image.read()
    if len(raw_bytes) > MAX_UPLOAD_BYTES:
        raise HTTPException(status_code=413, detail="Image is too large (maximum 10 MB)")
    result = await asyncio.to_thread(analyze_image, raw_bytes)

    ordered_labels = list(result["all_probs"].keys())
    tensor = [result["all_probs"][label] for label in ordered_labels]

    return {
        "label": result["label"],
        "confidence": result["confidence"],
        "labels": ordered_labels,
        "tensor": tensor,
        "all_probs": result["all_probs"],
    }


def analyze_image(raw_bytes: bytes):
    npimg = np.frombuffer(raw_bytes, np.uint8)
    img_bgr = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise HTTPException(status_code=400, detail="Could not decode image — file may be corrupted")

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    with model_lock:
        landmarks = get_5pt_landmarks(img_rgb)
        if landmarks is None:
            raise HTTPException(status_code=422, detail="No face detected in the image")
        aligned = predictor.align_face(img_bgr, landmarks)
        return predictor.predict(aligned)

@router.get("/health")
async def health():
    return {"status": "ok"}