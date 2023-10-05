import logging
import os
import sys

import colorama
import openai

from ui.ui_gr import main_gr_block

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d] %(message)s",
)

# if we are running in Docker
dockerflag = os.environ.get("dockerrun") == "yes"


if __name__ == "__main__":
    if not os.environ.get("OPENAI_API_KEY"):
        logging.error("Please give a api key!")
        sys.exit(1)

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    _port = int(sys.argv[1])

    gr_block = main_gr_block()

    logging.info(
        colorama.Back.GREEN
        + f"\n Visit http://localhost:{_port}"
          f"\n OpenAI Image Generation: https://platform.openai.com/docs/guides/images/introduction"
        + colorama.Style.RESET_ALL
    )
    if dockerflag:
        gr_block.queue(concurrency_count=1).launch(
            server_name="0.0.0.0",
            server_port=_port,
            share=False,
            favicon_path="./assets/favicon.ico"
        )
    else:
        gr_block.queue(concurrency_count=1).launch(
            server_name="0.0.0.0",
            server_port=_port,
            share=False
        )
