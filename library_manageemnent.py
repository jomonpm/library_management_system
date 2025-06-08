import random
import os

class User:
    existing_names_list = []
    existing_user_id_list = []
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
    
    @classmethod
    def check_user(cls):
         file_size = os.path.getsize("Library_users")
         with open("Library_users", "r") as file:
            if file_size !=0:
            
                for line in file:
                    existing_names, existing_user_id  = line.strip().split(",", 1)
                    cls.existing_names_list.append(existing_names)
                    cls.existing_user_id_list.append(existing_user_id)

                
    
    @classmethod
    def create_new_user(cls,name):
        cls.check_user()
        rand_num =random.randint(0,10000)
        user_id = str(rand_num) + name.strip(" ")
        
        if name not in cls.existing_names_list:
                
                with open("Library_users", "a") as file:
                    file.write(f"{name},{user_id}\n")
                print(f"Hello {name}, your User ID is {user_id}")
                user_exist = True
        else:
            print("Name already taken, try a new one")
            user_exist = False
        return user_exist
"""
    else:
        rand_num =random.randint(0,10000)
        user_id = str(rand_num) + name.strip(" ")

        
        with open("Library_users", "a") as file:
            file.write(f"{name},{user_id}\n")
        print(f"Hello new user {name}, your User ID is {user_id}")
        user_exist = True
    return user_exist
"""

class Member(User):
    def __init__(self,user_id,name):
        super().__init__(user_id,name)

class Librarian(User):
    def __init__(self,user_id,name):
        super().__init__(user_id,name)

class Management_system():
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
    @classmethod
    def book_borrow(cls,):
        pass

if __name__ == "__main__":
    flag = input("Hi..New User? (yes/no)")
    user_exist = False
    name = input("Please enter your name ")
    user_exist = User.create_new_user(name)
    while flag =="yes" and user_exist == False:
 
        name = input("Please enter your name ")
        user_exist = User.create_new_user(name)

    if flag == 'no':
        given_name = input("Enter name ")
        User.check_user()
        """
        with open("Library_users", "r") as file:    
            for line in file:
                existing_names, existing_user_id  = line.split(",", 1)
                User.existing_names_list.append(existing_names)
                User.existing_user_id_list.append(existing_user_id)
        """
        if given_name in User.existing_names_list:
            print(f"Hello {given_name}")
        else:
            print("Your name couldnot be found..Please create an account")

        

    