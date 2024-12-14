class Book:
    def __init__(self, title=None,author=None,year=None,genere=None,status=None) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.genere = genere
        self.status = status
    
    def __str__(self) -> str:
        return f"Title:{self.title} \nAuthor:{self.author} \nYear:{self.year} \nGenere:{self.genere}"# \nStatus: {self.status}"




