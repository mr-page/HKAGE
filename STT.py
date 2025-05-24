import base64
import requests



def audio2text(audio_file_path):
    with (open(audio_file_path,"rb") as audio_file):
        audio_data = audio_file.read()
        audio_base64 = base64.b64decode(audio_data).decode("uft-8")
        url = "https:''text.pollinations.ai/openai"
        prompt = "what's in this audio? Give me the text in traditional Chinese"
        payload = {
            "message":[
                {
                    "role": "user",
                    "content" : [
                        {"type": "text", "text" : prompt},
                        {
                            "type" : "input_audio",
                            "input_audio": {
                                "data" : audio_base64,
                                "format" : "mp3"
                            }
                        }
                    ]
                }
            ],
            "model" : "openai-audio"
        }
        response = requests.post(url=url,json=payload)
        return response.json()


