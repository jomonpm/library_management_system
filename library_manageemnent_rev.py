import random
import os
import csv

def add_books_to_file(new_book):   
    with open("Books_present", "a") as f:
            f.write(new_book)

def remove_books_from_file(to_be_removed_book):  
    with open("Books_present", "r") as f:
            lines = f.readlines()
    with open("Books_present", "w") as f:
        for line in lines:
            if line.strip() != to_be_removed_book:
                f.write(line) 

class Members:
    
    def __init__(self,user_name,user_id):
        self.user_id = user_id
        self.user_name = user_name
        self.borrow_book_history = []
    
    def create_new_user(self):
        with open("Library_users", "a") as file:
            file.write(f"{self.user_name},{self.user_id}\n")
        print(f"Hello {self.user_name}, your User ID is {self.user_id}")
    
    
    def borrow_book(self,book_borrow_name ):
        with open("borrow_details.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.user_name, book_borrow_name])
        #removing the borrowed books name from the available books
        remove_books_from_file(book_borrow_name)

        self.borrow_book_history.append(book_borrow_name)

    def return_book(self,return_book_name):

        with open("borrow_details.csv", "r") as f:
            rows = list(csv.reader(f))

        book_present = False

        for row in rows:
            if (row[0] == self.user_name and row[1] == return_book_name):
                book_present = True
        if book_present == True:
            updated_rows = [
            row for row in rows 
            if not (row[0] == self.user_name and row[1] == return_book_name)
        ]
            with open("borrow_details.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(updated_rows)
            
            with open("Books_present", "a") as f:
                f.write(return_book_name)
        else:
            print("The return details doesnot match >>..Try again")
            return 1
        
      


class Librarian(Members):
    def __init__(self,user_name,user_id):
        super().__init__(user_name,user_id)
    
    def add_books(self,new_book):
        add_books_to_file(new_book)
    
    def remove_books(self,to_be_removed_book):
        remove_books_from_file(to_be_removed_book)


def User_validation(file_name):
    
    existing_names_list = []
    existing_user_id_list = []
    
    existing_names_list.clear()
    existing_user_id_list.clear()
    
    file_size = os.path.getsize(file_name)
    with open(file_name, "r") as file:
        if file_size !=0:
        
            for line in file:
                existing_names, existing_user_id  = line.strip().split(",", 1)
                existing_names_list.append(existing_names)
                existing_user_id_list.append(existing_user_id)
    return existing_names_list, existing_user_id_list
    
def create_new_id(name):
    
    rand_num =random.randint(0,10000)
    user_id = str(rand_num) + name.strip(" ")
    
    return user_id


    
def accept_new_user_signup():
    name = input("Please enter your name ")
    user_id = create_new_id(name)
    return name, user_id
    
    
    

def existing_user_login(file_name):
    while True:
        given_name, user_id = input("Please enter your name and userID ").split()        
        existing_names_list, existing_user_id_list = User_validation(file_name)
        if given_name in existing_names_list:
            print(f"Hello {given_name}")

            break
    
        else:
            print("Name not found ...try again")
    return given_name, user_id  

def obj_creation(user_name, user_id, class_name):
    user_obj = class_name(user_name, user_id)
    return user_obj

def borrow_book_init(user_obj):
    with open('Books_present', 'r') as f:
        #print(f.read())
        available_books = f.read()
        
    while True:
        book_borrow_name = input("Enter the name of the book to borrow\n")
        if book_borrow_name in available_books:
            
            user_obj.borrow_book(book_borrow_name)
            break
        else:
            print("Book not found")

def return_book_init(user_obj):
    while True:
        return_book__name = input("Enter the name of the book to return\n")
        is_book_in_borrowlist = user_obj.return_book(return_book__name)
        if is_book_in_borrowlist !=1:
            break

def borrow_or_return_book(user_obj):
        value = input("Enter 1 to borrow a book \nEnter 2 to return a book")


        if value == "1":
            borrow_book_init(user_obj)
            
            
        else:
            return_book_init(user_obj)

def librarian_powers(user_name, user_obj):
    choice = input(f"Hello {user_name}, \nEnter your choice\n 1.Borrow book\n2.Return book\n3.Add book\n4.Remove book")
    
    if choice == "1":
        borrow_book_init(user_obj)
    
    elif choice == "2":
        return_book_init(user_obj)
    
    elif choice == "3":
        new_book = input("Enter the name of the book to add\n")
        user_obj.add_books(new_book)
    
    else:
        to_be_removed_book = input("Enter the name of the book to add\n")
        user_obj.remove_books(to_be_removed_book)


def main():
    choice = input("Hi..\nEnter your choice\nNew user = 1\nExisting user = 2\nLibrarian = 3\n")               
    
    
       
    if choice == "1":
        user_name, user_id = accept_new_user_signup() 
        user_obj = obj_creation(user_name, user_id, Members)
        user_obj.create_new_user()
        borrow_or_return_book(user_obj)

    elif choice == "2":
        
        user_name, user_id = existing_user_login("Library_users")
        user_obj = obj_creation(user_name, user_id, Members)  
        borrow_or_return_book(user_obj)
    else:
        user_name, user_id = existing_user_login("Librarian_details") #FOR LIBRARIAN
        user_obj = obj_creation(user_name, user_id, Librarian)
        librarian_powers(user_name, user_obj)
    

if __name__ == "__main__":
    main()
    

        
    
        