class library:
    def __init__(self,listofbooks):
        self.books=listofbooks
    
    def displayAvailablebooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("\t",book)
    def borrowbook(self,bookname):
        if bookname in self.books:
            print(f"you have been issued {bookname}. Keep it safe vand return in 15 days")
            self.books.remove(bookname)
            return True
        else:
            print("Book is either not available or issued to somebody")
            return False
    def returnbook(self,bookname):
        self.books.append(bookname)
        print("thanks for returning book")
class student:
    def requestbook(self):
        self.books = input("Enter the name of the book you want to borrow: ")
        return self.books
    def returnbook(self):
        self.books = input("Enter the name of the book you want to return: ")
        return self.books
if __name__ == "__main__":
    schoollibrary=library(["python","java","javascript","kotlin","ruby"])
    student=student()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a=int(input("enter your choice: "))
        if a==1:
            schoollibrary.displayAvailablebooks()
        elif a==2:
            schoollibrary.borrowbook(student.requestbook())
        elif a==3:
            schoollibrary.returnbook(student.returnbook())
        elif a==4:
            print("thanks")
            exit()
        else:
            print("invalid input")


