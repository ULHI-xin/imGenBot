import logging

import gradio as gr

from modules.image_gen_func import gen_image_from_prompt

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
)

# NOTE: Hacky trick to change the behavior of Gallery.postprocess()
#       Otherwise the generated image urls will be prepended with {host/file=} and
#       now the file redirect is problematic with url parameters.
gr.Gallery.postprocess = lambda s, x: x


def main_gr_block():
    with gr.Blocks() as entry:
        with gr.Row():
            with gr.Column():
                prompt = gr.Textbox(label="Prompt", lines=4)
            with gr.Column():
                size_picker = gr.Dropdown(
                    ['256x256', '512x512', '1024x1024'],
                    value='512x512',
                    label="Image Size",
                    info="The size of the generated images. "
                        "Must be one of 256x256, 512x512, or 1024x1024."
                    )
                n_slider = gr.Slider(
                    1, 10, value=1, step=1,
                    label="The number of images to generate. Must be between 1 and 10.")
        greet_btn = gr.Button("Generate")
        output = gr.Gallery(
            label="Generated images",
            show_label=False,
            elem_id="gallery"
        ).style(columns=(1, 2, 3, 4), object_fit="contain", height="auto")

        greet_btn.click(
            fn=gen_image_from_prompt,
            inputs=[prompt, size_picker, n_slider],
            outputs=output, api_name="gen_image_from_prompt")

    return entry
