import base64
import requests


def audio2text(audio_file_path):
    try:
        with open(audio_file_path, "rb") as audio_file:
            audio_data = audio_file.read()
            audio_base64 = base64.b64encode(audio_data).decode("utf-8")  # Fixed: encode instead of decode

            url = "https://text.pollinations.ai/openai"
            prompt = "what's in this audio? Give me the text in traditional Chinese"

            payload = {
                "messages": [  # Fixed: "message" → "messages" (API expects plural)
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "input_audio",
                                "input_audio": {
                                    "data": audio_base64,
                                    "format": "mp3"  # Ensure this matches your actual file format
                                }
                            }
                        ]
                    }
                ],
                "model": "openai-audio"
            }

            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

            response = requests.post(
                url=url,
                json=payload,
                headers=headers,
                timeout=30  # Added timeout
            )

            response.raise_for_status()  # Raises exception for 4XX/5XX errors
            return response.json()

    except FileNotFoundError:
        return {"error": f"Audio file not found: {audio_file_path}"}
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}


# Test the function
if __name__ == "__main__":
    result = audio2text("Test/Test.mp3")
    print(result["choices"][0]["message"]["content"])


