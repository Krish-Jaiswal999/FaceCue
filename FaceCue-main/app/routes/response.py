import os
from fastapi import APIRouter, HTTPException
from openai import OpenAI
from dotenv import load_dotenv
import app.pydantic_inputVerify.responseModel as response
import traceback
import asyncio

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is required; set it in .env before starting FaceCue")

router = APIRouter()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY,
)

MASTER_PROMPT = os.getenv('MASTER_PROMPT')


def build_user_message(
    analysis: response.EmotionAnalysis, target_emotion: str, user_message: str | None
) -> str:
    probs_formatted = "\n".join(
        f"  - {emotion}: {prob * 100:.2f}%"
        for emotion, prob in sorted(
            analysis.all_probs.items(), key=lambda x: x[1], reverse=True
        )
    )

    message_context = f"\nUser's follow-up message:\n{user_message}" if user_message else ""
    return f"""Current expression detected: **{analysis.label}** ({analysis.confidence * 100:.1f}% confidence)

Full probability breakdown:
{probs_formatted}

Target emotion the user wants to express: **{target_emotion}**

Please provide your coaching feedback.
{message_context}"""


@router.post("/response")
async def generate_response(body: response.ResponseRequest):
    if body.target_emotion not in [
        "Neutral", "Happy", "Sad", "Surprise", "Fear", "Disgust", "Angry"
    ]:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid target_emotion '{body.target_emotion}'. "
                   "Must be one of: Neutral, Happy, Sad, Surprise, Fear, Disgust, Angry",
        )
 
    user_message = build_user_message(body.analysis, body.target_emotion, body.message)
 
    try:
        if not MASTER_PROMPT:
            raise RuntimeError("Coaching service is not configured")

        chat_completion = await asyncio.to_thread(
            client.chat.completions.create,
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": MASTER_PROMPT},
                {"role": "user", "content": user_message},
            ],
            temperature=0.7,
            max_tokens=1800,
        )
 
        message = chat_completion.choices[0].message.content
        if not message:
            finish_reason = chat_completion.choices[0].finish_reason
            print(f"Empty response. Finish reason: {finish_reason}")
            return {"message": "Could not generate coaching feedback. Please try again."}

        return {"message": message}
 
    except Exception as e:
        traceback.print_exc()
        print("ERROR:", str(e))
        raise HTTPException(status_code=502, detail="Coaching service is temporarily unavailable")