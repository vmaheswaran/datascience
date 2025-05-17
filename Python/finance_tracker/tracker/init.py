import os

class Utils:
    def __init__(self):
        self.dir_path = os.path.dirname(os.path.abspath("F:\\python\\PythonBasics\\finance_tracker\\data\\"))
        print("Directory path : ", self.dir_path)
        self.log_file = "log.txt"
        self.transaction_file = "transaction.csv"
