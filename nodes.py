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


class Vui:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": ("MODEL",),
                "prompt": ("PROMPT",),
                "temperature": (
                    "FLOAT",
                    {
                        "default": 0.5,
                        "min": 0.1,
                        "max": 1.0,
                        "step": 0.1,
                    },
                ),
                "top_k": (
                    "INT",
                    {
                        "default": 100,
                        "min": 1,
                        "max": 200,
                        "step": 1,
                    },
                ),
                "top_p": (
                    "FLOAT",
                    {
                        "default": 0.9,
                        "min": 0.1,
                        "max": 1.0,
                        "step": 0.05,
                    },
                ),
                "max_duration": (
                    "INT",
                    {
                        "default": 120,
                        "min": 5,
                        "max": 120,
                        "step": 5,
                    },
                ),
            }
        }

    RETURN_TYPES = ("WAVEFORM",)
    RETURN_NAMES = ("waveform",)
    FUNCTION = "generate"
    CATEGORY = "Vui"

    def generate(self, model, prompt, temperature, top_k, top_p, max_duration):
        waveform = render(
            model,
            text=prompt,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            max_secs=max_duration,
        )

        return (waveform,)


class SaveVui:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "audio_path": ("STRING", {"default": "output.wav"}),
                "waveform": ("WAVEFORM",),
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ()
    FUNCTION = "save"
    CATEGORY = "Vui"

    def save(self, audio_path, waveform):

        torchaudio.save(audio_path, waveform[0], 22050)
        
        return ()

