from loginmgmt import *

print("Welcme to LMS system ..")
ip = input("Enter 1 for SignUp and 2 for SignIn: ")
if ip == "1":
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    pwd_hint = input("Enter password hint: ")
    signUp = SignUp()
    signUp.save_user(f_name, l_name, username, password, pwd_hint)
elif ip == "2":
    username = input("Enter username: ")
    password = input("Enter password: ")
    signIn = SignIn()
    signIn.enter_creds(username, password)
    