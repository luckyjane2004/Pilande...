class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: {self.title} by {self.author} ({self.year_published})")

# Create three book objects
book1 = Book("The Apothecary Diaries", "Natsu Hyuuga", 2011)
book2 = Book("One Piece", "Eiichiro Oda", 1997)
book3 = Book("Jujutsu Kaisen", "Gege Akutami ", 2018)

# Display book details
book1.describe()
book2.describe()
book3.describe()