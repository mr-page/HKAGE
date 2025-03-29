import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("请开始说话（10秒内）...")
        
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        
        try:
            audio = recognizer.listen(source, timeout=10)
            print("识别中...")
            text = recognizer.recognize_google(audio, language='zh-CN')
            print("\n识别结果：\n" + text)

        except sr.WaitTimeoutError:
            print("未检测到语音输入")
        except sr.UnknownValueError:
            print("无法识别语音内容")
        except sr.RequestError as e:
            print(f"服务请求失败；{e}")
        except Exception as e:
            print(f"发生未知错误：{e}")

if __name__ == "__main__":
    speech_to_text()