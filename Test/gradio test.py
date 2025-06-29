import gradio as gr
import requests
import base64
from io import BytesIO
import soundfile as sf
import os
import time
from typing import Optional


def process_audio(audio_path: Optional[str]) -> str:
    """Process audio and send to server with robust error handling"""
    # Validate audio input
    if audio_path is None or not os.path.exists(audio_path):
        return "請重新錄製音頻或上傳有效的音頻文件"

    # Ensure the file has content
    if os.path.getsize(audio_path) == 0:
        return "音頻文件為空，請重新錄製"

    # Retry mechanism for ngrok
    max_retries = 3
    retry_delay = 1  # seconds

    for attempt in range(max_retries):
        try:
            # Read and convert audio
            try:
                data, samplerate = sf.read(audio_path)
                with BytesIO() as mp3_buffer:
                    sf.write(mp3_buffer, data, samplerate, format='mp3')
                    audio_base64 = base64.b64encode(mp3_buffer.getvalue()).decode('utf-8')
            except Exception as e:
                return f"音頻處理失敗: {str(e)}"

            # Prepare request with timeout
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

            # Send to server
            response = requests.post(
                "https://instantly-beloved-griffon.ngrok-free.app/transcribe",
                json={"audio_data": audio_base64, "format": "mp3"},
                headers=headers,
                timeout=10  # Shorter timeout for faster retries
            )

            # Check response
            if response.status_code == 200:
                return response.json().get('text', '成功接收但無文本返回')
            else:
                if attempt < max_retries - 1:
                    time.sleep(retry_delay * (attempt + 1))  # Exponential backoff
                    continue
                return f"服務器錯誤 (HTTP {response.status_code}): {response.text}"

        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                time.sleep(retry_delay * (attempt + 1))
                continue
            return f"無法連接服務器: {str(e)}"
        except Exception as e:
            return f"處理過程中出現意外錯誤: {str(e)}"

    return "轉換失敗，請稍後再試"


def clear_and_prepare():
    """Clear previous state and prepare for new recording"""
    # This helps reset the audio input state
    return None, ""


with gr.Blocks(title="粵語轉換器", theme=gr.themes.Soft()) as app:
    gr.Markdown("""<h1 style='text-align: center'>🎤 粵語語音轉文字系統</h1>""")

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                label="請講廣東話",
                waveform_options={"waveform_progress_color": "#FF8800"},
                interactive=True
            )
            with gr.Row():
                submit_btn = gr.Button("開始轉換", variant="primary")
                clear_btn = gr.Button("清除重錄")

        with gr.Column():
            output_text = gr.Textbox(
                label="轉換結果",
                placeholder="繁體中文文本將顯示在此...",
                lines=5
            )

    # Event handlers
    submit_btn.click(
        fn=process_audio,
        inputs=audio_input,
        outputs=output_text,
        api_name="transcribe"
    )

    clear_btn.click(
        fn=clear_and_prepare,
        inputs=None,
        outputs=[audio_input, output_text],
        queue=False
    )

if __name__ == "__main__":
    app.launch(
        server_port=7860,
        share=True,
        show_error=True
    )
