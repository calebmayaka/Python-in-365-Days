class book:
    
    book_counter = 0
    def __init__(self,name,author):
        self.name = name
        self.author = author
    
    book_counter += 1
    
    def nameandauthor(self):
        print(f"the name of the book is {self.name} and the author is {self.author}")
    

input_name = str(input("enter book's name: "))
input_author = str(input("enter book's name: "))

book1 = book(input_name,input_author)

print(book1.nameandauthor())
print(book.book_counter)

        

        