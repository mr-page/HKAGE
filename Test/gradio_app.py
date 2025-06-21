import gradio as gr
import requests
import base64
from io import BytesIO
import soundfile as sf


def process_audio(audio_path):
    """Process audio and send to server"""
    try:
        # 1. Read audio and convert to MP3 in memory
        data, samplerate = sf.read(audio_path)
        with BytesIO() as mp3_buffer:
            sf.write(mp3_buffer, data, samplerate, format='mp3')
            audio_base64 = base64.b64encode(mp3_buffer.getvalue()).decode('utf-8')

        # 2. Send to server
        response = requests.post(
            "http://localhost:8000/transcribe",
            json={"audio_data": audio_base64, "format": "mp3"},
            timeout=30
        )

        return response.json()['text'] if response.status_code == 200 else f"Error: {response.text}"

    except Exception as e:
        return f"Processing error: {str(e)}"


with gr.Blocks(title="粵語轉換器", theme=gr.themes.Soft()) as app:
    gr.Markdown("""<h1 style='text-align: center'>🎤 粵語語音轉文字系統</h1>""")

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["microphone"],
                type="filepath",
                label="請講廣東話",
                waveform_options={"waveform_progress_color": "#FF8800"}
            )
            submit_btn = gr.Button("開始轉換", variant="primary")

        with gr.Column():
            output_text = gr.Textbox(
                label="轉換結果",
                placeholder="繁體中文文本將顯示在此...",
                lines=5
            )

    submit_btn.click(
        fn=process_audio,
        inputs=audio_input,
        outputs=output_text
    )

if __name__ == "__main__":
    app.launch(server_port=7860)
