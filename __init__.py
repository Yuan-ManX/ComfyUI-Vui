from .nodes import LoadVuiModel, LoadVuiPrompt, Vui, SaveVui

NODE_CLASS_MAPPINGS = {
    "LoadVuiModel": LoadVuiModel,
    "LoadVuiPrompt": LoadVuiPrompt,
    "Vui": Vui,
    "SaveVui": SaveVui,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadVuiModel": "Load Vui Model",
    "LoadVuiPrompt": "Load Vui Prompt",
    "Vui": "Vui",
    "SaveVui": "Save Vui",
} 

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
