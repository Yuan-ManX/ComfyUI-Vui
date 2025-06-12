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


