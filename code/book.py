class book:
    increment = 1.10
    books_available  = 0

    def __init__(self,author,name,price,pubdate):
        self.author = author
        self.name = name
        self.price = price
        self.pubdate = pubdate
        
    books_available +=1
        
    def price_increment(self):
        self.price = self.price * book.increment
        return self.price
                      
author_input = str(input("enter the name of the author: "))
name_input = str(input("enter the name of the author: "))
price_input = int(input("enter the name of the author: "))
pubdate_input = int(input("enter the name of the author: "))

book1 = book(author_input,name_input,price_input,pubdate_input)

print(f"this book is called {book1.name} and the author is {book1.author} it was published in {book1.pubdate} it costs {book1.price}")

book1.price_increment()

print(f"the new price is {book1.price}")
print(f"total number of books availabe is {book.books_available}")
