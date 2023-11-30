from ex_3.HomeworkHandler import HomeworkHandler

class Factorize(HomeworkHandler):
    def __init__(self):
        super().__init__(2, 'Function factorize, using processes')
        
    def run(self):
        string = input("Please enter list of numbers separated by ', ':")
        print(string)