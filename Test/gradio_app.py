import gradio as gr
import requests
import ffmpeg
from datetime import datetime


def transcribe_cantonese(audio_path):
    """Optimized for Cantonese audio files"""
    try:
        with open(audio_path, "rb") as f:
            files = {"file": f}
            response = requests.post(
                "https://instantly-beloved-griffon.ngrok-free.app/transcribe",
                files=files,
                timeout=30
            )
        return response.json()['text']
    except Exception as e:
        return f"Error: {str(e)}"


with gr.Blocks(title="粵語轉換器", theme=gr.themes.Soft()) as app:
    gr.Markdown("""<h1 style='text-align: center'>🎤 粵語語音轉文字系統</h1>""")

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["microphone", "upload"],
                type="filepath",
                label="錄音或上傳音頻",
                waveform_options={"waveform_progress_color": "#FF8800"}
            )
            submit_btn = gr.Button("開始轉換", variant="primary")

        with gr.Column():
            output_text = gr.Textbox(
                label="轉換結果",
                placeholder="繁體中文文本將顯示在此...",
                lines=8
            )

    submit_btn.click(
        fn=transcribe_cantonese,
        inputs=audio_input,
        outputs=output_text
    )

if __name__ == "__main__":
    app.launch(server_port=7860, share=True)
