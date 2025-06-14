import random
import os

class Members:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name

    def borrow_book():
        pass

    def return_book():
        pass
        

class Librarian(Members):
    def __init__(self,user_id,name):
        super().__init__(user_id,name)


class User_validation:
    existing_names_list = []
    existing_user_id_list = []
    
    
    @classmethod
    def check_user(cls):
        cls.existing_names_list.clear()
        cls.existing_user_id_list.clear()
        
        file_size = os.path.getsize("Library_users")
        with open("Library_users", "r") as file:
            if file_size !=0:
            
                for line in file:
                    existing_names, existing_user_id  = line.strip().split(",", 1)
                    cls.existing_names_list.append(existing_names)
                    cls.existing_user_id_list.append(existing_user_id)

    @classmethod
    def create_new_user(cls,name):
        
        rand_num =random.randint(0,10000)
        user_id = str(rand_num) + name.strip(" ")
        
        with open("Library_users", "a") as file:
            file.write(f"{name},{user_id}\n")
        print(f"Hello {name}, your User ID is {user_id}")


if __name__ == "__main__":
    
    flag = input("Hi..New User? (yes/no)")
   
    def accept_new_user():
        name = input("Please enter your name ")
        User_validation.create_new_user(name)
        
    def existing_user():
        while True:
            given_name = input("Please enter your name ")
            User_validation.check_user()
            
            if given_name in User_validation.existing_names_list:
                print(f"Hello {given_name}")
                break
            else:
                print("Name not found ...try again")
                    
    if flag =="yes":
         accept_new_user()  
    else:
         existing_user()  
    

        
    
        