from ex_3.HomeworkHandler import HomeworkHandler

class Cleaner(HomeworkHandler):
    def __init__(self):
        super().__init__(1, "Folder cleaner, using Treads")
        
    def run(self):
        string = input('Please enter path to folder:')
        print(string)