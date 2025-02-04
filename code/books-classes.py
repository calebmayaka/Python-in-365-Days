class Book():
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre
    
    def printdetails(self):
        print(f"This book is {self.title} is by {self.author} and it is in the {self.genre} genre ")
        
book1 = Book("Memories We Lost", "Chris Wanjala", "Short story")
book2 = Book("The River and The Source", "Margeret Ogot", "novel")
book3 = Book("Tumbo Lisiloshiba", "walibora", "hadithi fupi") 

print(book1.author) 
print(book2.title)     
print(book2.printdetails()) 