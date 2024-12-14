from os import listdir
from typing import List
import re

class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []
    
    def add_new_user(self,user) -> str:
        if any(existing_user.email == user.email for existing_user in self.users):
            return f"The user {user.name} already exist"
        else:
            self.users.append(user)
            return f"The user {user.name} is add with success"   

    def get_user(self,email) -> str:
        for user in self.users:
            if user.email == email:
                return user.name
        return "This user no exit"

    def show_all_users(self):
        i = 1
        if not self.users:
            return "No users registered"

        usuarios = []

        for user in self.users:
            usuarios.append(f"[{i}] Name: {user.name} \n    Email: {user.email}\n")
            i += 1
        return "\n".join(usuarios)
    
    def get_info_book(self,indice):
        return self.books[int(indice) - 1]

    def add_new_book(self,book) -> str:
        if book in self.books:
            return f"The book {book.title} existsded "
        else:
            self.books.append(book)
            return f"The book {book.title} add the library"
    
    def singin_user(self,email,password) -> bool:
        print(len(self.users))
        for user in self.users:
            print(email)
            if user.email == email and user.password == password:
                return True
        return False
    
    def type_users(self,email) -> int:
        for user in self.users:
            if user.email == email:
                return user.type_user
        return 3

    def show_books(self):
        i = 1
        if not self.books:
            return "No books registered"

        books = []

        for book in self.books:
            if book.status != "Lended":
                books.append(f"[{i}] Title: {book.title} ")#\nAuthor: {book.author} \nYear: {book.year} \nGenere: {book.genere}")
                i += 1
        return "\n".join(books)
    
    def show_books_all(self):
        i = 1 
        if not self.books:
            return "No books registered"
        
        books = []

        for book in self.books:
            books.append(f"[{i}] Title: {book.title} \n    Author: {book.author} \n    Year: {book.year} \n    Genere: {book.genere} \n    Status: {book.status} \n")
            i += 1
        return "\n".join(books)

    def show_author(self):
        i = 1
        authors_not_dupplicate = set()
        formater = []

        for author in self.books:
            if author.author not in authors_not_dupplicate:
                authors_not_dupplicate.add(author.author)
                formater.append(f"[{i}] {author.author}")
                i += 1
        return "\n".join(formater)

    def get_author(self,index):
        list_authors = self.show_author()
        list_author = list_authors.split("\n")
        author = re.sub(r"\[\d+\]","",list_author[int(index) - 1])
        return author.strip() 
    
    def get_book_author(self,author):
        i = 1
        books = []
        for book in self.books:
            if book.author == author:
                books.append(f"[{i}] Title: {book.title} \n    Author: {book.author}")
                i += 1
        return "\n".join(books)
    
    def get_name_by_autor(self,index,author):
        list_books = self.get_book_author(author)
        list_book = list_books.split("\n")
        name_book = re.sub(r"\[\d+\]","",list_book[int(index) - 1])
        name_book = name_book.replace("Title:","")
        
        for book in self.books:
            if book.title == name_book.strip():
                return book
        return f"Book not find"

    def show_years(self):
        i = 1
        year_not_dupplicate = set()
        formater = []

        for year in self.books:
            if year.year not in year_not_dupplicate:
                year_not_dupplicate.add(year.year)
                formater.append(f"[{i}] {year.year}")
                i += 1
        return "\n".join(formater)

    def get_year(self,index):
        list_years = self.show_years()
        list_year = list_years.split("\n")
        year = re.sub(r"\[\d+\]","",list_year[int(index) - 1])
        return year.strip()

    def get_books_year(self,year):
        i = 1
        books = []
        for book in self.books:
            if book.year == year:
                books.append(f"[{i}] Title: {book.title} \n    Year: {book.year}")
                i += 1 
        return "\n".join(books)

    def get_name_by_year(self,index,year):
        list_years = self.get_books_year(year)
        list_year = list_years.split("\n")
        name_book = re.sub(r"\[\d+\]","",list_year[int(index) - 1])
        name_book = name_book.replace("Title:","")
        
        for book in self.books:
            if book.title == name_book.strip():
                return book
        return f"Book not find" 
    
    def show_genere(self):
        i = 1
        genere_not_dupplicate = set()
        formater = []

        for genere in self.books:
            if genere.year not in genere_not_dupplicate:
                genere_not_dupplicate.add(genere.year)
                formater.append(f"[{i}] {genere.genere}")
                i += 1
        return "\n".join(formater)

    def get_genere(self,index):
        list_generes = self.show_genere()
        list_genere = list_generes.split("\n")
        genere = re.sub(r"\[\d+\]","",list_genere[int(index) - 1])
        return genere.strip() 
    
    def get_books_genere(self,genere):
        i = 1
        books = []
        for book in self.books:
            if book.genere == genere:
                books.append(f"[{i}] Title: {book.title} \n    Year: {book.genere}")
                i += 1 
        return "\n".join(books)
    
    def get_name_by_genere(self,index,genere):
        list_generes = self.get_books_genere(genere)
        list_genere = list_generes.split("\n")
        name_book = re.sub(r"\[\d+\]","",list_genere[int(index) - 1])
        name_book = name_book.replace("Title:","")
        
        for book in self.books:
            if book.title == name_book.strip():
                return book
        return f"Book not find"  

    def lend_books(self,index,book) -> str:
        for book1 in self.books:
            if book.title == book1.title:
                self.books[int(index) - 1].status = "Lended"
                return f"The book {book.title} is borrowed"
        return f"We haven´t this book"

    def return_books(self,index,book) -> str:
        for book1 in self.books:
            if book.title == book1.title:
                self.books[int(index) - 1].status = "Available"
                return f"The book {book.title} has been returned"     
        return f"The book {book.title} this not borrowed"
    
    def get_title_book(self): 
        title_not_dupplicate = set()
        formater = []

        for book in self.books:
            if book.title not in title_not_dupplicate:
                title_not_dupplicate.add(book.title)
                formater.append(f"{book.title}")
        
        return formater
    
    def get_author_book(self,index):
        title_book = self.get_title_book()
        title_book = title_book[int(index) - 1] 

        for book in self.books:
            if book.title == title_book:
                return book.author
        return f"We haven't this book"

    def edit_title_book(self,index,title):
        title_book = self.get_title_book()
        title_book = title_book[int(index) - 1]
        for book in self.books:
            if book.title == title_book:
                self.books[int(index) - 1].title = title
                return f"Title changed successfully"
        return f"We haven´t this book"

    def edit_author_book(self,index,title,author):
        for book in self.books:
            if book.title == title:
                self.books[int(index) - 1].author = author
                return f"Author changed successfully"
        return f"We haven't this book"

    def get_year_book(self,index): 
        title_book = self.get_title_book()
        title_book = title_book[int(index) - 1]

        for book in self.books:
            if book.title == title_book:
                return book.year
        return f"We haven't this book"

    def edit_year_book(self,index,title,year):
        for book in self.books:
            if book.title == title:
                self.books[int(index) - 1].year = year
                return f"Year changed successfully"
        return f"We haven't this book"

    def get_genere_book(self,index):
        title_book = self.get_title_book()
        title_book = title_book[int(index) - 1]

        for book in self.books:
            if book.title == title_book:
                return book.genere
        return f"We haven't this book"
    
    def edit_genere_book(self,index,title,genere):
        for book in self.books:
            if book.title == title:
                self.books[int(index) - 1].genere = genere
                return f"Year changed successfully"
        return f"We haven't this book"

    def get_email(self):
        email_not_dupplicate = set()
        formater = []

        for users in self.users:
            if users.email not in email_not_dupplicate:
                email_not_dupplicate.add(users.email)
                formater.append(f"{users.email}")
        
        return formater

    def edit_email(self,index,email):
        email_user = self.get_title_book()
        email_user = email_user[int(index) - 1]
        for user in self.users:
            if user.email == email_user:
                self.users[int(index) - 1].email = email
                return f"Title changed successfully"
        return f"We haven´t this book"

    def get_name(self,index):
        list_name = self.get_email()
        list_name = list_name[int(index) - 1]

        for user in self.users:
            if user.email == list_name:
                return user.name
        return f"We haven't this user"

    def edit_name(self,index,email,new_name):
        for user in self.users:
            if user.email == email:
                self.users[int(index) - 1].name = new_name
                return f"Year changed successfully"
        return f"We haven't this user"

    def get_password(self,index):
        email = self.get_email()
        email = email[int(index) - 1]

        for user in self.users:
            if user.email == email:
                return user.password
        return f"We haven't this user"

    def edit_password(self,index,email,new_password):
        for user in self.users:
            if user.email == email:
                self.users[int(index) - 1].password = new_password
                return f"Year changed successfully"
        return f"We haven't this user"



