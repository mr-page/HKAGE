from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import base64
import requests
from pydantic import BaseModel
from six import BytesIO
import soundfile as sf

app = FastAPI(title="Cantonese Transcription API")

class TranscriptionResponse(BaseModel):
    text: str
    tokens_used: int

@app.post("/transcribe", response_model=TranscriptionResponse)
async def transcribe_cantonese(
    file: UploadFile = File(...),  # Required file upload
    prompt: str = Form("將以下粵語音頻轉換為繁體中文文本")  # Default Cantonese prompt
):
    """
    Endpoint specifically for Cantonese audio transcription
    """
    try:
        # Read and encode audio
        # audio_data = await file.read()
        # audio_base64 = base64.b64encode(audio_data).decode('utf-8')
        file_format = file.filename.split('.')[-1]

        def audio2base(audio):
            sample_rate, audio_data = audio
            with BytesIO() as buffer:
                sf.write(buffer,audio_data, sample_rate, format='mp3')
                audio_bytes = buffer.getvalue()

            base64_encoded  = base64.b64encode(audio_bytes).decode('utf-8')
            return base64_encoded

        audio_base64 = audio2base(file)

        # Prepare payload optimized for Cantonese
        payload = {
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "input_audio",
                        "input_audio": {
                            "data": audio_base64,
                            "format": file_format
                        }
                    }
                ]
            }],
            "model": "openai-audio",
            "language": "yue"  # Force Cantonese processing
        }

        # Call transcription API
        response = requests.post(
            "https://text.pollinations.ai/openai",
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()

        return {
            "text": result['choices'][0]['message']['content'],
            "tokens_used": result['usage']['total_tokens']
        }

    except Exception as e:
        raise HTTPException(500, f"Cantonese transcription failed: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
