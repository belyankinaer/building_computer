class VideoCard:
    def __init__(self, name: str, vram: int = None, frequency: int = None):
        self._name = name
        self._vram = vram
        self._frequency = frequency

    def get_name(self):
        return self._name

    def get_config(self):
        return {
            "name": self._name,
            "vram": self._vram,
            "frequency": self._frequency
        }
