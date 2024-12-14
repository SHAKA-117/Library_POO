import os, sys, time
from book import Book
from library import Library
from user import User

def borrar_lineas(numero_de_lineas):
    for _ in range(numero_de_lineas):
  # Mover el cursor una línea hacia arriba
        sys.stdout.write("\033[F")  
        # Borrar la línea actual
        sys.stdout.write("\033[K")
    sys.stdout.flush()

def show_books_library(library:Library,usuario:User):
    while True:
        os.system("clear")
        print("Books of Library")
        print(library.show_books())
        print(" ")
        print("[1] Borrow a book \n[2] Return")
        option = input(str("Select an Option: "))
        match(option):
            case "1":
                borrar_lineas(3)
                index = input(str("Select a book: "))
                book =  library.get_info_book(index)
                print(library.lend_books(index,book))
                usuario.lend_books_user(book)
                print("Return a main menu")
                time.sleep(5)
                return
            case "2":
                return 
            case _:
                os.system("clear")
                print("Incorrect option")
                time.sleep(5)

def my_books(library:Library,usuario:User):
    while True:
        os.system("clear")
        print("My books")
        print(usuario.show_my_books())
        print(" ")
        print("[1] Return book \n[2] Return")
        option = input(str("Select a option: "))
        match(option):
            case "1":
                borrar_lineas(3)
                book = usuario.get_info_book(option)
                print(usuario.return_books_user(book))
                library.return_books(option,book)
                print("Return a main menu")
                time.sleep(5)
                return
            case "2":
                return
            case _:
                os.system("clear")
                print("Incorrect option")

def filter_author(library:Library,usuario:User):
    while True:
        os.system("clear")
        print("Filter book by Author")
        print(library.show_author())
        print(" ")
        option = input("Select at author: ")
        author = library.get_author(option)
        os.system("clear")
        print(library.get_book_author(author))
        print(" ")
        print("[1] Borrow a book \n[2] Return")
        option = input(str("Select an Option: "))
        match(option):
            case "1":
                borrar_lineas(3)
                index = input(str("Select a book: "))
                book =  library.get_name_by_autor(index,author)
                print(library.lend_books(index,book))
                usuario.lend_books_user(book)
                print("Return a main menu")
                time.sleep(5)
                return
            case "2":
                return
            case _:
                os.system("clear")
                print("Incorrect option")
                time.sleep(5)

def filter_year(library:Library,usuario:User):
    while True:
        os.system("clear")
        print("Filter book by Year")
        print(library.show_years())
        print(" ")
        option = input("Select at year: ")
        year = library.get_year(option)
        os.system("clear")
        print(library.get_books_year(year))
        print(" ")
        print("[1] Borrow a book \n[2] Return")
        option = input(str("Select an Option: "))
        match(option):
            case "1":
                borrar_lineas(3)
                index = input(str("Select a book: "))
                book =  library.get_name_by_year(index,year)
                print(library.lend_books(index,book))
                usuario.lend_books_user(book)
                print("Return a main menu")
                time.sleep(5)
                return
            case "2":
                return
            case _:
                os.system("clear")
                print("Incorrect option")
                time.sleep(5)

def filter_genere(library:Library,usuario:User):
    while True:
        os.system("clear")
        print("Filter book by Genere")
        print(library.show_genere())
        print(" ")
        option = input("Select at year: ")
        genere = library.get_genere(option)
        os.system("clear")
        print(library.get_books_genere(genere))
        print(" ")
        print("[1] Borrow a book \n[2] Return")
        option = input(str("Select an Option: "))
        match(option):
            case "1":
                borrar_lineas(3)
                index = input(str("Select a book: "))
                book =  library.get_name_by_genere(index,genere)
                print(library.lend_books(index,book))
                usuario.lend_books_user(book)
                print("Return a main menu")
                time.sleep(5)
                return
            case "2":
                return
            case _:
                os.system("clear")
                print("Incorrect option")
                time.sleep(5)

def show_books_filter(library:Library,usuario:User):
    while True:
        os.system("clear")
        print("Filter book by")
        print(f"[1] Author \n[2] Year \n[3] Genere \n[4] Return")
        option = input(str("Select a option: "))
        match(option):
            case "1":
                filter_author(library,usuario)       
            case "2": 
                filter_year(library,usuario)
            case "3":
                filter_genere(library,usuario)
            case "4":
                return
            case _:
                os.system("clear")
                print("Incorrect option")
                time.sleep(5)

def Loging(library:Library) -> None:
    os.system("clear")
    print("Plese insert your data")
    name = input(str("Name: "))
    email = input(str("Email: "))
    password = input(str("Password: "))
    os.system("clear")
    user = User(name,password,email,2)
    print(library.add_new_user(user))
    print("Return a Main menu...")
    time.sleep(5)

def menu_user(library:Library,user) -> None:
    while True:
        os.system("clear")
        print(f"Welcome {user}")
        print("[1] Show books in library \n[2] My books \n[3] Seach Bocks by filter \n[4] lon out")
        print(" ")
        option = input(str("Select an option: "))
        match(option):
            case "1":
                os.system("clear")
                print("Books in library\n")
                library.show_books()
            case "2":
                my_books(library,usuario)
            case "3":
                show_books_filter(library,usuario)
            case "4":
                return
            case _:
                os.system("clear")
                print("Incorrect option")
                time.sleep(5)

def add_new_book(library:Library):
    while True:
        os.system("clear")
        print("Write data new book")
        title = input(f"Title of book new: ")
        author = input(f"Name of author: ")
        year = input(f"Year of publication: ")
        genere = input(f"Name of genere: ")
        print(" ")
        while True:
            result = input(f"The data of book is correct? [y/n]: ").strip().lower()
            if result == "y":
                new_book = Book(title,author,year,genere,"Available") 
                print(library.add_new_book(new_book))
                print("Return to main menu...")
                time.sleep(3)
                return
            elif result == "n":
                print("Re-enter the data for the new book")
                time.sleep(2)
                break
            else:
                borrar_lineas(1)
                print("Invalid option. Plese type 'y' or 'n'")
                time.sleep(2)
                borrar_lineas(1)

def show_books_admin(library:Library):
    while True:
        os.system("clear")
        print("Books in library")
        print(library.show_books_all())
        time.sleep(10)
        while True:
            result = input(f"The data of user is correct? [y/n]: ").strip().lower()
            if result == "y":
                return
            elif result == "n":
                break
            else:
                borrar_lineas(1)
                print("Invalid option. Plese type 'y' or 'n'")
                time.sleep(2)
                borrar_lineas(2)


def edit_title(library:Library,index):
    title = library.get_title_book()
    print("Old title:",title[int(index) - 1])
    option = input("New Title: ")
    print(library.edit_title_book(index,option))
    print("Return Main menu")
    time.sleep(5)
    return

def edit_author(library:Library,index):
    author = library.get_author_book(index)
    title = library.get_title_book()
    print("Old author:",author)
    option = input("New Author: ")
    print(library.edit_author_book(index,title[int(index) - 1],option))
    print("Return Main menu")
    time.sleep(5)
    return

def edit_year(library:Library,index):
    year = library.get_year_book(index)
    title = library.get_title_book()
    print("Old year:",year)
    option = input("New Author: ")
    print(library.edit_year_book(index,title[int(index) -1],option))
    print("Return Main menu")
    time.sleep(5)
    return

def edit_genere(library:Library,index):
    genere = library.get_genere_book(index)
    title = library.get_title_book()
    print("Old genere:",genere)
    option = input("New genere: ")
    print(library.edit_genere_book(index,title[int(index) - 1],option))
    print("Return Main menu")
    time.sleep(5)
    return


def menu_edit_admin(library:Library,index):
    while True:
        os.system("clear")
        print("[1] Edit Title \n[2] Edit Author \n[3] Edit Year \n[4] Edit Genere \n[5] Return")
        print(" ")
        option = input("Select an option: ")
        match(option):
            case "1":
                edit_title(library,index)
                return
            case "2":
                edit_author(library,index)
                return
            case "3":
                edit_year(library,index)
                return
            case "4":
                edit_genere(library,index)
                return
            case "5":
                return
            case _:
                os.system("clear")
                print("Password or user incorrect")
                time.sleep(3)

def menu_book_admin(library:Library):
    while True:
        os.system("clear")
        print("[1] Add new book \n[2] Show Books \n[3] Edit data book \n[4] Return")
        print(" ")
        option = input(str("Select Option: "))
        match(option):
            case "1":
                add_new_book(library)
            case "2":
                show_books_admin(library)
            case "3":
                os.system("clear")
                print(library.show_books_all())
                option = input("Select book for edit: ")
                menu_edit_admin(library,option)
            case "4":
                return
            case _:
                os.system("clear")
                print("Password or user incorrect")
                time.sleep(3)
                return

def menu_new_user(library:Library):
    while True:
        os.system("clear")
        print("Write data new user")
        name = input(f"New user name: ")
        password = input(f"Password of user: ")
        email = input(f"Write email: ")
        print(" ")
        while True:
            result = input(f"The data of user is correct? [y/n]: ").strip().lower()
            if result == "y":
                new_user = User(name,password,email,2) 
                print(library.add_new_user(new_user))
                print("Return to main menu...")
                time.sleep(3)
                return
            elif result == "n":
                print("Re-enter the data for the new book")
                time.sleep(2)
                break
            else:
                borrar_lineas(1) 
                print("Invalid option. Plese type 'y' or 'n'")
                time.sleep(2)
                borrar_lineas(1)

def menu_show_user(library):
    while True:
        os.system("clear")
        print("Registered users")
        print(library.show_all_users())
        while True:
            result = input(f"Do you want to come back? [y/n]: ").strip().lower()
            if result == "y":
                return
            elif result == "n":
                break
            else:
                borrar_lineas(1)
                print("Invalid option. Plese type 'y' or 'n'")
                time.sleep(2)
                borrar_lineas(2)

def edit_name(library:Library,index):
    email = library.get_email()
    name = library.get_name(index)
    print("Old name:",name)
    option = input("New Author: ")
    print(library.edit_name(index,email[int(index) - 1],option))
    print("Return Main menu")
    time.sleep(5)
    return

def edit_password(library:Library,index):
    password = library.get_password(index)
    email = library.get_email()
    print("Old password:",password)
    option = input("New Author: ")
    print(library.edit_password(index,email[int(index) - 1],option))
    print("Return Main menu")
    time.sleep(5)
    return

def edit_email(library:Library,index):
    email = library.get_email()
    print("Old email:",email[int(index) - 1])
    option = input("New email: ")
    print(library.edit_title_book(index,option))
    print("Return Main menu")
    time.sleep(5)
    return

def menu_edit_user(library:Library,index):
    while True:
        os.system("clear")
        print("[1] Edit Name \n[2] Edit Password \n[3] Edit Email \n[4] Return")
        option = input("Select an option: ")
        match(option):
            case "1":
                edit_name(library,index)
                return
            case "2":
                edit_password(library,index)
                return
            case "3":
                edit_email(library,index)
                return
            case "4":
                return
            case _:
                os.system("clear")
                print("Password or user incorrect")
                time.sleep(3)
 
def menu_user_admin(library:Library):
    while True:
        os.system("clear")
        print("[1] Add new user \n[2] show user \n[3] Edit data user \n[4] Return")
        print(" ")
        option = input(str("Select Option: "))
        match(option):
            case "1":
                menu_new_user(library)
            case "2":
                menu_show_user(library)
            case "3":
                os.system("clear")
                print(library.show_all_users())
                option = input("Select book for edit: ")
                menu_edit_user(library,option)
            case "4":
                return
            case _:
                os.system("clear")
                print("Password or user incorrect")
                time.sleep(3)

def menu_admin(library:Library,user):
    while True:
        os.system("clear")
        print(f"Welcome {user}")
        print("[1] Books \n[2] Users \n[3] Lon out")
        print(" ")
        option = input(str("Select Option: "))
        match(option):
            case "1": 
                os.system("clear")
                menu_book_admin(library)
            case "2":
                menu_user_admin(library) 
            case "3":
                return
            case _:
                os.system("clear")
                print("Password or user incorrect")
                time.sleep(3)
                
def Sing_In(library:Library) -> None:
    while True:
        os.system("clear")
        print("Library v0.1")
        print("Plese insert your data")
        email = input(str("Email: "))
        password = input(str("Password: "))
        login = library.singin_user(email,password)
        user = library.get_user(email)
        if login == True:
            if library.type_users(email) == 1:
                menu_admin(library,user)
                return
            elif library.type_users(email) == 2:
                menu_user(library,user)
                return
        else:
            os.system("clear")
            print("Password or user incorrect")
            time.sleep(3)
            
def Main_Menu(library:Library) -> None:
    while True:
        os.system("clear")
        print("[1] Loging \n[2] Sing in \n[3] Exit")
        print(" ")
        option = input(str(f"Select an Option: ")) 
        match(option):
            case "1":
                Loging(library)
            case "2":
                Sing_In(library)
            case "3":
                print("Goodbye")
                exit()
            case _:
                os.system("clear")
                print("Incorrect option")

library = Library()
usuario = User()
book = Book()
app = Book("Harry Potter", "Neitan","1998","Infantil","Available")
library.add_new_book(app)
app2 = Book("Cien Años de Soledad", "Gabriel García Márquez", "1967", "Novela","Available")
library.add_new_book(app2)
app3 = Book("El Principito", "Antoine de Saint-Exupéry", "1943", "Fantasía","Lended")
library.add_new_book(app3)
user = User("Israel Cruz Hernadez","1234","israel@hotmail.com",1) 
library.add_new_user(user)
user2 = User("Pedro Gomez Gomez","1234","pedro@hotmail.com",2)
library.add_new_user(user2)
Main_Menu(library)


