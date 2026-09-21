from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parent.parent
WEIGHTS = ROOT / "ddamfn" / "weights" / "rafdb.pth"
IMAGE = ROOT / "test" / "face.jpg"
LANDMARKER = ROOT / "face_landmarker.task"

@pytest.mark.skipif(
    not (WEIGHTS.exists() and IMAGE.exists() and LANDMARKER.exists()),
    reason="requires the model weights, face_landmarker.task, and test/face.jpg",
)
def test_ddamfn_pipeline():
    import cv2
    import mediapipe as mp
    import numpy as np
    from mediapipe.tasks import python as mp_python
    from mediapipe.tasks.python import vision
    from ddamfn.infer import DDAMFNPredictor

    base_options = mp_python.BaseOptions(model_asset_path=str(LANDMARKER))
    options = vision.FaceLandmarkerOptions(base_options=base_options, num_faces=1)
    landmarker = vision.FaceLandmarker.create_from_options(options)
    image = cv2.imread(str(IMAGE))
    assert image is not None
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)
    result = landmarker.detect(mp_image)
    assert result.face_landmarks

    landmark_indices = (33, 263, 1, 61, 291)
    height, width = image_rgb.shape[:2]
    landmarks = np.array(
        [[result.face_landmarks[0][index].x * width,
          result.face_landmarks[0][index].y * height] for index in landmark_indices],
        dtype=np.float32,
    )
    predictor = DDAMFNPredictor(str(WEIGHTS))
    aligned = predictor.align_face(image, landmarks)
    prediction = predictor.predict(aligned)
    assert prediction["label"]