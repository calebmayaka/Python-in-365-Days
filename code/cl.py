class book:
    def __init__(self,name,author):
        self.name = name
        self.author = author
        
    def Details (self):
        print(f"the book name is {self.name} and the author is {self.author}")
    
input_name = str(input("enter the book name:"))

input_author = str(input("enter the book name:"))

book1 = book(input_name,input_author)

print(book1.name)

print(book1.Details())

