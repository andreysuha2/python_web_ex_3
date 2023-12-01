from pick import pick
from .HomeworkHandler import HomeworkHandler
from .part_1.main import Cleaner
from .part_2.main import Factorize

class App:
    def __init__(self, pick: pick, title: str, handlers: list[HomeworkHandler]) -> None:
        self.title = title
        self.handlers = handlers
        self.pick = pick
        
    @property
    def pick_options(self) -> list[str]:
        return list(map(lambda handler: f'part {handler.part_number}. {handler.description}', self.handlers))
    
    def run(self) -> None:
        option, index = self.pick(self.pick_options, self.title)
        print(f"Runing handler: {option}")
        handler = self.handlers[index]
        handler.run()
        
def main() -> None:
    app = App(
        title = 'Please choose part of home work:',
        handlers=[ Cleaner(), Factorize() ],
        pick=pick
    )
    app.run()

if __name__ == "__main__":
    main()