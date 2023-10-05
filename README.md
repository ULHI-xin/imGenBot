A very simple Gradio-based UI wrapper for AI images generation.

Supported APIs or platforms:
- [OpenAI DALL·E models](https://platform.openai.com/docs/guides/images/introduction])


## Quick start:

### Prerequisites:

- Python version 3.9+ (3.8 may be enough as well but not fully tested)
- OpenAI API key

### Start local service:

Install all requirements:
```sh
% pip install -r requirements.txt
```

Set OpenAI API key in current environment:
```sh
% export OPENAI_API_KEY={YOUR_OPENAI_API_KEY}
```

Start with the main entry point `main.py`, by specifying local http port:
```sh
% python3 main.py 2333
```