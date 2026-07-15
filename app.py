import gradio as gr
from summarizer import summarize, STYLE_PROMPTS

with gr.Blocks(title="SiteSense") as demo:

    gr.Markdown("# 🔎 SiteSense")
    gr.Markdown("Summarize any website in seconds")

    with gr.Row():
        url = gr.Textbox(
            label="🌐 Website URL",
            placeholder="https://example.com",
            scale=4
        )

        style = gr.Dropdown(
            choices=list(STYLE_PROMPTS.keys()),
            value="Friendly 😊",
            label="Summary Style",
            scale=1
        )

    button = gr.Button("✨ Summarize", variant="primary")

    output = gr.Markdown(label="Summary")

    button.click(
        fn=summarize,
        inputs=[url, style],
        outputs=output
    )

demo.launch(share=True)