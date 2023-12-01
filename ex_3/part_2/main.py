from ex_3.HomeworkHandler import HomeworkHandler
from abc import ABCMeta, abstractclassmethod
from functools import wraps 
from time import time
from multiprocessing import cpu_count, Pool

def time_measuring(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> list[list, float]:
            time_start = time()
            result = func(*args, **kwargs)
            return [ result,  time() - time_start ]
        return wrapper

class NumDividers():
    def __init__(self, number: int) -> None:
        self.num = number
    
    def get(self):
        return [ num for num in range(1, self.num + 1) if self.num % num == 0 ]
    
    def __str__(self) -> str:
        return f"num: {self.num}, deviders: {', '.join([ str(n) for n in self.get() ])}"
    
    def __repr__(self) -> str:
        return str(self)

class Factorize(HomeworkHandler):
    def __init__(self) -> None:
        super().__init__(2, 'Function factorize, using processes')
        
    def run(self) -> None:
        string = input("Please enter list of numbers separated by ', ': ")
        lst = list(map(lambda i: NumDividers(int(i.strip())), string.split(", ")))
        sync_factorize = FactorizeHandlerSync(lst)
        proccess_factorize = FactorizeHandlerProccess(lst)
        sync_factorize.run()
        print("")
        proccess_factorize.run()
        
class FactorizeHandler(metaclass=ABCMeta):
    def __init__(self, lst: list[NumDividers], working_type: str) -> None:
        self.lst = lst
        self.working_type = working_type
    
    @abstractclassmethod
    def calculate(self):
        pass
    
    def run(self) -> None:
        results, worked = self.calculate()
        print("Factorize: ", self.working_type)
        print("results:")
        for result in results:
            print(result)
        print("working during: ", worked)

class FactorizeHandlerSync(FactorizeHandler):
    def __init__(self, lst: list[NumDividers]) -> None:
        super().__init__(lst, working_type="Synchronical")
    
    @time_measuring
    def calculate(self) -> list[str]:
        return [ str(dividers) for dividers in self.lst ]
    
class FactorizeHandlerProccess(FactorizeHandler):
    def __init__(self, lst: list[NumDividers]) -> None:
        self.count_cpu = cpu_count()
        super().__init__(lst, working_type="Using processess")
        
    def get_diveders(self, num: NumDividers) -> str:
        return str(num)
    
    @time_measuring
    def calculate(self) -> list[str]:
        with Pool(processes=self.count_cpu) as pool:
            return list(pool.map(self.get_diveders, self.lst))