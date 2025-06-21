import base64
import requests

with open('Test.mp3', "rb") as audio_file:
    audio_data = audio_file.read()
    audio_base64 = base64.b64encode(audio_data).decode("utf-8")
    url = "https://text.pollinations.ai/openai"
    prompt = "what's in this audio? Give me the text in traditional chinese"
    payload = {
        'message': [
            {
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
            }
        ],
        "model": "openai-audio"
    }
response = requests.post(url='https://pollination.ai/openai',json =payload)
print(response)

