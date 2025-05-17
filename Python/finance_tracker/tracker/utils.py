import os
from datetime import datetime

class Logger:
    def __init__(self):
        self.log_file = os.path.join(os.path.dirname("F:\\python\\PythonBasics\\finance_tracker\\data\\"), "tracker.log")

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{datetime.now()} - {message}\n")
