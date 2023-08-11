from random import randint


class new:
    def __init__(self, pwd, ph):
        self.pwd = pwd
        self.ph_num = ph


class Homepage:
    def __init__(self):
        self.__user_dict = {}
        print(f"{'**** Welcome in Login/SignIn ****' : ^130}\n")

    def sigIn(self):
        print("****************************************************************************************")
        while True:
            username = str(input("\nEnter your name : ").strip(
                " ").capitalize()+str(randint(100, 999)))
            username = username.replace(" ", "")
            if username not in self.__user_dict:
                break
        ph_num = self.get_int("Enter your Mobile number : ", 10)
        pwd = self.setpwd("Create a Password : ")
        new_user = new(pwd, ph_num)
        self.__user_dict[username] = new_user
        print(f"\n--> UserId : {username} \n--> Registered Successfully")
        print("****************************************************************************************")

    def login(self):
        print("****************************************************************************************")
        username = input("\nEnter UserId : ")
        pwd = self.setpwd("Enter Your Password : ")
        if username in self.__user_dict:
            if self.__user_dict[username].pwd == pwd:
                print("\nAuthentication Completed [This is your content]: \n")
                with open("Private_content.txt", "r") as f:
                    print(f.read())
            else:
                print("**Invalid Password***")
        else:
            print("**Invalid username***")
        print("****************************************************************************************")

    def forgot(self):
        print("****************************************************************************************")
        username = str(input("\nEnter your name : ").strip(" ").capitalize()).replace(" ", "")
        ph_num = self.get_int("Enter your Mobile number : ", 10)

        for user in self.__user_dict:
            if username == user[0:-3]:
                if self.__user_dict[user].ph_num == ph_num:
                    print("\n-> Verification Completed : ")
                    self.__user_dict[user].pwd=self.setpwd("Creating New Password : ")
                    print(f"-> Password changed successfully\nUserId : {user}\nPassword : {self.__user_dict[user].pwd}")
                    return
                else:
                    print("-> Invalid Mobile Number !")
        print("-> Invalid Name Entered !")
        

    def menu(self):
        while True:
            print(
                "****************************************************************************************")
            print("\nEnter Your choice : \n(1)-> SignIn New User\n(2)-> Login Existing User\n(3)-> Forgot Password")
            choice = self.get_int("\nEnter Your choice : ", 1)
            print(
                "****************************************************************************************")

            if choice < 1 or choice > 3:
                return False

            elif choice == 1:
                print("\n*********** SigIn New User**********")
                self.sigIn()

            else:
                if self.__user_dict:
                    if choice == 2:
                        print("\n*********** Login Existing User**********")
                        self.login()

                    elif choice == 3:
                        self.forgot()

                else:
                    print("\nNo User Data Available")

    def setpwd(self,text):
        while True:
            pswd = input(text)
            res = True
            if (len(pswd) >= 8):
                if any(char.isupper() for char in pswd):
                    pass
                else:
                    print("Atleast 1 character in uppercase...")
                    res = False
                if any(char.islower() for char in pswd):
                    pass
                else:
                    print("Atleast 1 character in lowercase...")
                    res = False
                if any(char.isdigit() for char in pswd):
                    pass
                else:
                    print("Atleast 1 character is digit 1 to 9...")
                    res = False
                if any(char in "@#$%^&*_?" for char in pswd):
                    pass
                else:
                    print("Atleast 1 character is special...")
                    res = False
            else:
                print("Password length should be equal or more than 8")
                res = False

            if res == True:
                return pswd

    def get_int(self, text, limit):
        while True:
            try:
                key = int(input(text))
                if len(str(key)) == limit:
                    key = str(key).replace(" ", "")
                    return int(key)
                else:
                    print(f"\n-->Input Length must be {limit} digits long\n")

            except:
                print("Invalid Input (Please enter integers only)")


s = Homepage()
s.menu()
 