from computer_composition import ComputerComposition

composition = ComputerComposition("Мой ПК")
composition.create({
    "processor": {"name": "Intel i7", "cores": 8, "frequency": 3.6},
    "video_card": {"name": "RTX 3060", "vram": 12},
    "memory": {"name": "Corsair Vengeance", "capacity": 16, "frequency": 3200},
    "ssd": {"name": "Samsung 970", "capacity": 500, "interface": "NVMe"},
    "motherboard": {"name": "ASUS Prime", "chipset": "B560"},
    "power_supply": {"name": "Corsair RM750", "wattage": 750},
    "cooler": {"name": "Noctua NH-D15", "quantity": 2}
})

composition.get_composition()
