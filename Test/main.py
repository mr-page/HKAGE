from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import base64
import requests
from pydantic import BaseModel
from io import BytesIO
import soundfile as sf
import json

app = FastAPI(title="Cantonese Transcription API")


class TranscriptionResponse(BaseModel):
    text: str
    tokens_used: int


@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_cantonese(
        file: UploadFile = File(...),
        prompt: str = Form("將以下粵語音頻轉換為繁體中文文本，如果不能請解釋")
):
    try:
        # 1. Read and convert audio
        audio_data = await file.read()
        file_format = file.filename.split('.')[-1].lower()

        if file_format != 'mp3':
            with BytesIO(audio_data) as input_buffer:
                data, samplerate = sf.read(input_buffer)
                with BytesIO() as output_buffer:
                    sf.write(output_buffer, data, samplerate, format='mp3')
                    audio_data = output_buffer.getvalue()

        # 2. Prepare API request
        audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        payload = {
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "input_audio",
                        "input_audio": {
                            "data": audio_base64,
                            "format": "mp3"
                        }
                    }
                ]
            }],
            "model": "openai-audio",
            "language": "yue"
        }

        # 3. Call API and parse response
        response = requests.post(
            "https://text.pollinations.ai/openai",
            json=payload,
            timeout=30
        )

        # Handle non-JSON responses
        try:
            result = response.json()
        except json.JSONDecodeError:
            raise HTTPException(502, f"Invalid API response: {response.text}")

        # 4. Extract and validate transcription
        if not isinstance(result, dict):
            raise HTTPException(502, "Unexpected API response format")

        try:
            content = result['choices'][0]['message']['content']
            tokens = result['usage']['total_tokens']
            return {
                "text": content,
                "tokens_used": tokens
            }
        except (KeyError, IndexError) as e:
            raise HTTPException(502, f"Missing expected fields in response: {str(e)}")

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, f"Processing failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
