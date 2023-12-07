class book:
    
    book_counter = 0
    def _init__(self,name,author):
        self.name = name
        self.author = author
    
    book_counter += 1
    
    def nameandauthor(self):
        print(f"the name of the book is {self.name} and the author is {self.author}")
    

input_name = str(input("enter book's name: "))
input_author = str(input("enter book's name: "))

ook1 = book(input_name,input_author)
        

        