class User:
    def __init__(self,name=None,password=None,email=None,type_user=None) -> None:
        self.name = name
        self.password = password
        self.email = email
        self.type_user = type_user
        self.borrowed_book = []
   
    def __str__(self) -> str:
        return f"{self.name} {self.password} {self.email} {self.type_user}"

    def get_info_book(self,indice):
        return self.borrowed_book[1-int(indice)]

    def lend_books_user(self,book) -> bool:
        if book.title not in self.borrowed_book:
            self.borrowed_book.append(book)
            return False
        else:
            return True
         
    def return_books_user(self,book) -> None:
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)

    def show_my_books(self):
        i = 1
        if not self.borrowed_book:
            return "You're not has books lend"

        books = []
        
        for book in self.borrowed_book:
            books.append(f"[{i}] Title: {book.title}") #\nAuthor: {book.author} \nYear: {book.year} \nGenere: {book.genere} \nStatus: {book.status}")
        return "\n".join(books)

