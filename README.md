# ComfyUI-Vui

ComfyUI-Vui is now available in ComfyUI, [Vui](https://github.com/fluxions-ai/vui) is a llama based transformer that predicts audio tokens.



## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Vui.git
```

3. Install dependencies:
```
cd ComfyUI-Vui
pip install -r requirements.txt
```


## Model


### Download Pretrained Models


Direct3D-S2 Pretrained [Models](https://huggingface.co/fluxions/vui)

Vui.BASE is base checkpoint trained on 40k hours of audio conversations

Vui.ABRAHAM is a single speaker model that can reply with context awareness.

Vui.COHOST is checkpoint with two speakers that can talk to each other.
