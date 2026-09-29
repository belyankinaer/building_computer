class Processor:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name


class VideoCard:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name


class Memory:
    def __init__(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name


class ComputerComposition:
    def __init__(self, name: str):
        self.__name = name
        self.__composition = []

    def create(self, processor: str, video_card: str, memory: str):
        processor = Processor(processor)
        video_card = VideoCard(video_card)
        memory = Memory(memory)

        self.__composition = [processor, video_card, memory]

        print('Ваша сборка:')
        for component in self.__composition:
            print(f"{component.get_name()}")


computer = ComputerComposition('Сборка 1')
computer.create(processor='процессор', video_card='видеокарта', memory='память')
