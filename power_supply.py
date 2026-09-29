class PowerSupply:
    def __init__(self, name: str, wattage: int = None, modularity: str = None):
        self._name = name
        self._wattage = wattage
        self._modularity = modularity

    def get_name(self):
        return self._name

    def get_config(self):
        return {
            "name": self._name,
            "wattage": self._wattage,
            "modularity": self._modularity
        }
