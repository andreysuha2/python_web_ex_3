from abc import ABCMeta, abstractclassmethod

class HomeworkHandler(metaclass=ABCMeta):
    def __init__(self, part_number: int, description: str):
        self.part_number = part_number
        self.description = description
        
    @abstractclassmethod
    def run(self, *args, **kwargs) -> None:
        pass