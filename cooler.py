class Cooler:
    def __init__(self, name: str, cooler_type: str = None, max_rpm: int = None, quantity: int = 1):
        self._name = name
        self._cooler_type = cooler_type
        self._max_rpm = max_rpm
        self._quantity = quantity

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def get_config(self):
        return {
            "name": self._name,
            "cooler_type": self._cooler_type,
            "max_rpm": self._max_rpm,
            "quantity": self._quantity
        }
