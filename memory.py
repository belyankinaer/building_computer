class Memory:
    def __init__(self, name: str, capacity: int = None, frequency: int = None):
        self._name = name
        self._capacity = capacity
        self._frequency = frequency

    def get_name(self):
        return self._name

    def get_config(self):
        return {
            "name": self._name,
            "capacity": self._capacity,
            "frequency": self._frequency
        }
