import sys
from tracker.utils import *
from tracker.transaction import *
from tracker import *

user = input("Hi there! Welcome to Finance tracker. Please enter your userid : ")
print(f"Welcome {user}. This program will help you track your income, expense and financial report.")
ip = input("Please enter your option 1. Income 2. Expense 3. Report : ").upper()
if ip == "INCOME":
    print("You have selected Income option.")
    type = ip
    cat = input("Enter income category 1. Finance 2. Job 3. Business 4. Others : ")
    if cat == "1":
        category = "Finance"
    elif cat == "2":
        category = "Job"
    elif cat == "3":
        category = "Business"
    elif cat == "4":
        category = "Others"
    else:
        print("Invalid category entered. Please enter a valid category.")
        sys.exit(1)
    amount = input(f"Please enter your {ip} amount : ")
    save_transaction = Transaction(user, type, category, amount)
    save_transaction.save_transaction()
    print(f"Your {ip} of {amount} added in database..")

elif ip == "EXPENSE":
    print("You have selected Expense option.")
    type = ip
    cat = input("Enter expense category 1. Food 2. Bills 3. Medicines 4. Others : ")
    if cat == "1":
        category = "Food"
    elif cat == "2":
        category = "Bills"
    elif cat == "3":
        category = "Medicines"
    else:
        category = "Others"
    amount = -1 * int(input(f"Please enter your {ip} amount : "))
    save_transaction = Transaction(user, type, category, amount)
    save_transaction.save_transaction()
    print("Your {} of {} added in database..".format(ip,amount))

elif ip == "REPORT":
    print("You have selected Report option.")
    trans = Transaction(user, "", "", "")
    txn = trans.get_txt()
    for item in txn:
        print(item)
    print("Now lets see the breakdown by category.")
    txn_by_cat = Transaction(user, "", "", "")
    txn = txn_by_cat.get_txn_by_cat()
    for item in txn:
        print(item)
else:
    print("Invalid option. Please enter a valid option.")
    sys.exit(1)
