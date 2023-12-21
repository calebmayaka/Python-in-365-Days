class book:
    def __init__(self,name,author,dop):
        self.name = name
        self.author = author
        self.dop = dop
        
    def printdata(self):
        print(f"the name of the book is {self.name} written by {self.author} and it was published in the year {self.dop}")
        
        
input_name = str(input("enter the book name: "))
input_author = str(input("enter the author name: "))
input_dop = int(input("enter the date of publication: "))

book1 = book(input_name,input_author,input_dop)

book.printdata()