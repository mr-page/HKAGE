from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import base64
from io import BytesIO

app = FastAPI(title="Cantonese Transcription API")


class TranscriptionRequest(BaseModel):
    audio_data: str  # base64 encoded audio
    format: str  # audio format (mp3/wav)


class TranscriptionResponse(BaseModel):
    text: str


@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_cantonese(request: TranscriptionRequest):
    try:
        # 1. Call Pollinations.ai API directly
        response = requests.post(
            "https://text.pollinations.ai/openai",
            json={
                "messages": [{
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Transcribe this Cantonese audio to Traditional Chinese"},
                        {
                            "type": "input_audio",
                            "input_audio": {
                                "data": request.audio_data,
                                "format": request.format
                            }
                        }
                    ]
                }],
                "model": "openai-audio",
                "language": "yue"
            },
            timeout=30
        )

        # 2. Validate response
        result = response.json()
        if "choices" not in result:
            raise HTTPException(502, "Invalid API response")

        return {"text": result['choices'][0]['message']['content']}

    except requests.exceptions.RequestException as e:
        raise HTTPException(502, f"API request failed: {str(e)}")
    except Exception as e:
        raise HTTPException(500, f"Processing failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)




