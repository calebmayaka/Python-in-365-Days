class book:
    def __init__(self,bookname,bookauthor,pubdate):
        self.bookname = bookname                #this is a instance variable.They are set using the set keyword
        self.bookauthor = bookauthor
        self.pubdate = pubdate
        
    def adddate(self):
        newdate = self.pubdate + 10
        return newdate

name_input = str(input("enter your name: "))
book1 = book("python fundamentals",name_input,2024)

print(book1)
print(f"Bookname {book1.bookname} and the author is {book1.bookauthor}")
print(book1.adddate())