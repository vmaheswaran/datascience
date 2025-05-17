import os
import csv
from datetime import datetime
#from tracker.init import *
from tracker.utils import *

class Transaction:
    def __init__(self, user_id, transaction_type, category, amount):
        self.user_id = user_id
        self.transaction_type = transaction_type
        self.category = category
        self.amount = amount
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_file = os.path.join(os.path.dirname("F:\\python\\PythonBasics\\finance_tracker\\data\\"), "transaction.csv")
    
    def save_transaction(self):
        with open(self.transaction_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.user_id, self.transaction_type, self.category, self.amount, self.timestamp])
            loggger = Logger()
            loggger.log(f"Transaction saved: {self.user_id}, {self.transaction_type}, {self.category}, {self.amount}, {self.timestamp}")

    def get_txt(self):
        transactions = []
        print("Transaction history for : " + self.user_id )
        with open(self.transaction_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.user_id:
                    transactions.append(row)
        return transactions
    
    def get_txn_by_cat(self):
        transactions = []
        sum_inc = 0
        sum_exp = 0
        with open(self.transaction_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == self.user_id and row[1] == "INCOME":
                        sum_inc += float(row[3])
                if row[0] == self.user_id and row[1] == "EXPENSE":
                        sum_exp += float(row[3])
            transactions.append(self.user_id +" Total income is : "+ str(sum_inc))
            transactions.append(self.user_id +" Total expense is : "+ str(sum_exp))
            transactions.append(self.user_id +" Total balance is : "+ str(sum_inc + sum_exp))
        return transactions
