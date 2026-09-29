class Motherboard:
    def __init__(self, name: str, chipset: str = None, socket: str = None):
        self._name = name
        self._chipset = chipset
        self._socket = socket

    def get_name(self):
        return self._name

    def get_config(self):
        return {
            "name": self._name,
            "chipset": self._chipset,
            "socket": self._socket
        }
