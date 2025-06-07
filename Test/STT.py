import requests

with open("test2.mp3", "rb") as f:
    response = requests.post(
        " https://instantly-beloved-griffon.ngrok-free.app/transcribe",
        files={"file": f},
        data={"language": "zh-HK", "prompt": "Transcribe precisely"}
    )
print(response.json())
