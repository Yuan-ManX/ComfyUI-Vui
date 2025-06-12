import torchaudio

from vui.inference import render
from vui.model import Vui


class LoadVuiModel:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model_path": ("STRING", {"default": "fluxions/vui"}),
                "device": (["cuda", "cpu"], {"default": "cuda"}),
            }
        }

    RETURN_TYPES = ("MODEL",)
    RETURN_NAMES = ("model",)
    FUNCTION = "load_model"
    CATEGORY = "Vui"

    def load_model(self, model_path, device):
        model = Vui.from_pretrained(model_path).cuda()
        
        return (model,)


class LoadVuiPrompt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {
                    "default": "Hey, here is some random stuff, usually something quite long as the shorter the text the less likely the model can cope!",
                    "multiline": True
                }),
            }
        }

    RETURN_TYPES = ("PROMPT",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "load_prompt"
    CATEGORY = "Vui"

    def load_prompt(self, text):
        prompt = text
        
        return (prompt,)

