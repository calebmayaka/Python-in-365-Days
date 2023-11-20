#class variables are variables that are shared by all the instanced in the class

class book:
    number_of_books = 0                         # this is a class variable
    price_increment = 1.15
    
    def __init__(self,bookname,bookauthor,pubdate,price):
        self.bookname = bookname                #this is a instance variable.They are set using the set keyword
        self.bookauthor = bookauthor
        self.pubdate = pubdate
        self.price = price
        
        book.number_of_books += 1
        
    def increment_price(self):
        self.price = self.price * book.price_increment
        return self.price
    
    @classmethod  # this is a decorator
    def new_price_increment(cls,new_incr):               # im using this class method to modify the price increment
        cls.price_increment = new_incr

name_input = str(input("enter your name: "))

price_input = int(input("enter book price: "))

book1 = book("python fundamentals",name_input,2024,price_input)

book.new_price_increment(1.25)

print(f"Bookname {book1.bookname} and the author is {book1.bookauthor} and the price is {book1.price}")

print(f"price before increment is {book1.price}")
book1.increment_price()
print(f"new price is {book1.price} from the {book1.price_increment} price increment")

print(book.number_of_books)