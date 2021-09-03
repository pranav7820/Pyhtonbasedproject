class libararry:
    def __init__(self,list,name) :
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displaybook(self):
        print(f"We have following books in our librarry :{self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender book database has been updated , you can take the book now")
        else :
            print(f"book is already being used by {self.lendDict[book]}")
    
    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added to the list")

    def returnbook(self,book):
        self.booklist.remove(book)    


 
pnna=libararry(["python","rich Daddy poor Daddy","harry potter","c++ basics","algorithm by CLRS"],"code with harry")     

while True:
    print(f"welcome to the {pnna.name} library.enter your choice to continue")
    print("1. Display Books")
    print("2. lend a Books")
    print("3. add a Books")
    print("4. return a Books")
    user_choice=int(input())

    if user_choice ==1:
        pnna.displaybook()

    if user_choice ==2:
        book =input("enter the book you want to land:")
        user = input("enter your name:2")
        pnna.lendbook(user,book)
    if user_choice ==3:
            book = input("enter the book you want to add:")
            pnna.addbook(book)
    if user_choice ==4:
        book = input("enter the book you want to add:")
        pnna.addbook(book)
    else:
        print("not a valid option")

        print("press q to quite and c to continue")
        user_choice2 =input()
    if user_choice2=="q":
            exit()
    elif user_choice2=="c":
            continue