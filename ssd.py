class SSD:
    def __init__(self, name: str, capacity: int = None, interface: str = None):
        self._name = name
        self._capacity = capacity
        self._interface = interface

    def get_name(self):
        return self._name

    def get_config(self):
        return {
            "name": self._name,
            "capacity": self._capacity,
            "interface": self._interface
        }
