from cooler import Cooler
from memory import Memory
from motherboard import Motherboard
from power_supply import PowerSupply
from processor import Processor
from ssd import SSD
from video_card import VideoCard


class ComputerComposition:
    def __init__(self, name: str):
        self._name = name
        self._composition = []

    def get_name(self):
        return self._name

    def get_composition(self):
        print('Ваша сборка:')
        for component in self._composition:
            print(f"  {component.get_name()}")
            config = component.get_config()
            for key, value in config.items():
                if value is not None:
                    print(f"    {key}: {value}")

    def create(self, components: dict):
        mapping = {
            'processor': Processor,
            'video_card': VideoCard,
            'memory': Memory,
            'ssd': SSD,
            'motherboard': Motherboard,
            'power_supply': PowerSupply,
            'cooler': Cooler
        }
        for key, params in components.items():
            name = params.pop('name')
            self._composition.append(mapping[key](name, **params))
