import base64
import requests


def cantonese_stt(audio_path):
    """Convert Cantonese audio to text using Pollinations.ai"""
    with open(audio_path, "rb") as f:
        audio_base64 = base64.b64encode(f.read()).decode("utf-8")

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
                            "data": audio_base64,
                            "format": "mp3"  # or "wav"
                        }
                    }
                ]
            }],
            "model": "openai-audio",
            "language": "yue"  # Cantonese
        },
        timeout=30
    )

    return response.json()['choices'][0]['message']['content']


# Usage
text = cantonese_stt("Test.mp3")
print(f"Transcription: {text}")
