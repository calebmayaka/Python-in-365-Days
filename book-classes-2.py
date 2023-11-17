class Book:
    total_books = 0  # Class variable to keep track of the total number of books

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        Book.total_books += 1  # Increment the total number of books when a new instance is created

    def display_info(self):
        return f"{self.title} by {self.author}. Genre: {self.genre}"

    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Creating instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Classics")

# Displaying book information and total number of books
print(book1.display_info())  # Display book1 info
print(book2.display_info())  # Display book2 info

print(f"Total number of books in the library: {Book.get_total_books()}")
