import base64
import requests
def audio2text(audio_file_path):
    with open(audio_file_path,"rb") as audio_file:
        audio_data = audio_file.read()
        audio_base64 = base64.b64encode(audio_data).decode("utf-8")
        url = "https://text.pollinations.ai/openai"
        prompt = "what's in this audio? Give me the text in traditional chinese"
        payload = {
            'messages' : [
                {
                    "role" : "user",
                    "content" : [
                        {"type" : "text","text": prompt },
                        {
                            "type" : "input_audio",
                            "input_audio" : {
                                "data"  : audio_base64,
                                "format" : "mp3"
                            }
                        }
                    ]
                }
            ],
            "model":"openai-audio"
        }
        response = requests.post(url=url, json=payload)
        return response.json()


result= audio2text("Test.mp3")
print(result['choices'][0])

