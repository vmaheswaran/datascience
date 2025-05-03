import os

class Utils():
    def __init__(self):
        self.dir_path = "F:\\python\\Files\\Nested\\LMS"
        self.cred_file = "credentials.txt"
        self.post_file = "post.txt"

    def loadAllPost(self, username, file_name):
        full_path = os.path.join(self.dir_path, file_name)
        if os.path.exists(full_path):
            with open(full_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if username in line:
                        print("Post for user {}: {}".format(username, line.strip()))
                    
    def load_credentials(self, username, file_name):
        full_path = os.path.join(self.dir_path, file_name)
        cred_check = False
        if os.path.exists(full_path):
            with open(full_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if username in line:
                        cred_check = True
                        return cred_check

    def check_credentials(self, username, password, file_name):
        full_path = os.path.join(self.dir_path, file_name)
        cred_check = False
        if os.path.exists(full_path):
            with open(full_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if username in line and password in line:
                        cred_check = True
                        return cred_check

    def write_to_file(self, id, info, file_name):
        full_path = os.path.join(self.dir_path, file_name)
        if os.path.exists(self.dir_path):
            with open(full_path, "a") as file:
                content = file.write(str(info) + "\n")
                print("User {} added successfully".format(info[id]["username"]))
        else:
            print(f"File not found: {full_path}")

class SignIn(Utils):
    def enter_creds(self, username, password):
        cred_utils = Utils.check_credentials(self, username, password, "credentials.txt")
        utils = Utils()
        if cred_utils:
            print("Welcome {} to LMS ".format(username))
            while True :
                ip = input("Do you want to post message now? (y/n): ")
                postit = PostIt()
                if ip.lower() == 'y':
                    msg = input("Enter your post : ")
                    postit.save_post(username, msg)
                elif ip.lower() == 'n':
                    op = input("Do you want to see all posts? (y/n): ")
                    if op.lower() == 'y':
                        print("Sure, here are your posts :")
                        utils.loadAllPost(username, "post.txt")
                        print("Thank you for using LMS")
                        break
                    else:
                     print("Thank you for using LMS")
                     break
                else:
                    print("Invalid input, please enter 'y' or 'n'")
        else:
            print("Invalid credentials, please try again")

class SignUp(Utils):
    def save_user(self, f_name, l_name, username, password, pwd_hint):
        id = username
        util = Utils()
        check_user_exist = util.load_credentials(username, "credentials.txt")
        if check_user_exist:
            print("User already exists, please try again")
            return
        else:
            info = {
                id: {
                    "f_name": f_name,
                    "l_name": l_name,
                    "username": username,
                    "password": password,
                    "pwd_hint": pwd_hint
                }
            }
        util.write_to_file(id, info, "credentials.txt")

class PostIt(Utils):
    def save_post(self, username, post):
        id = username
        info = {
            id: {
                "username": username,
                "post": post
            }
        }
        util = Utils()
        util.write_to_file(id, info, "post.txt")
    