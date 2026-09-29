class Processor:
    def __init__(self, name: str, cores: int = None, frequency: float = None):
        self._name = name
        self._cores = cores
        self._frequency = frequency

    def get_name(self):
        return self._name

    def get_config(self):
        return {
            "name": self._name,
            "cores": self._cores,
            "frequency": self._frequency
        }
