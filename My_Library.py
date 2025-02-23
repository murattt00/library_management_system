
def readline():
    with open("books.txt", "r") as x:
        lines = x.readlines()
        return lines
    
def add_book():
    bks = open("books.txt", "a")
    isbn_num = input("Enter ISBN Number: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    new_book = str(isbn_num + ", " + book_name + ", " + author +"," +" F\n")
    bks.write(new_book)
    bks.close()
    print("Book added!")
    return 

def add_student():
    std = open("students.txt", "a")
    std_no = input("Enter Student Number: ")
    std_name = input("Enter Stundet Name: ")
    std_lname = input("ENter  Student Last Name: ")
    new_std = str(std_no + ", " + std_name + " " + std_lname + "\n")
    std.write(new_std)
    std.close()
    print("Student Added!")
    return 

def book_search_by_isbn():
    isbn = input("Enter the ISBN number: ")
    lines = readline()
    cnt = 0
    for line in lines:
        book = line.strip().split(",")
        if isbn == book[0]:
            cnt = 1
            print("Book Faund: ")
            print(line)
            break
    if cnt == 0:
        print("There isn't a book with ISBN number " + isbn )
    choice = input("Do you want to search again(Y or N): ")
    if choice.upper() == "Y":
        return book_search_by_isbn()
    else:
        return 
    
def book_search_by_name():
    name = input("Enter the name of book that you looking for: ")
    namelower = name.strip().lower()
    lines = readline()
    cnt = 0
    for line in lines:
        book = line.strip().split(",")
        bOne = book[1].strip().lower()
        if namelower in bOne:
            cnt = cnt + 1
            print("Book Faund: ")
            print(line)    
    if cnt == 0:
        print("There isn't a book with the name " + name)
    choice = input("Do you want to search again(Y or N): ")
    if choice.upper() == "Y":
        return book_search_by_name()
    else:
        return  

def all_books():
    lines = readline()
    cnt = 1
    for line in lines:
        print(str(cnt) + ")" + line)
        cnt = cnt + 1
    return 

def all_checked_books():
    lines = readline()
    cnt = 1
    for line in lines:
        book = line.strip().split(",")
        if book[-1] == " T":
            print(str(cnt) + ")" + line)
            cnt = cnt + 1
    if cnt == 1:
        print("There aren't any checked book!")
    return 
 
def delete_book():
    lines = readline()
    cnt = 1
    for line in lines:
        print(str(cnt) + ")" + line)
        cnt  = cnt + 1
    del_book = int(input("Enter the number of book that you want to delete: "))
    if 1 <= del_book <= len(lines):
        book = lines[del_book -1].strip().split(",")
        if book[-1] != " T":
            del lines[del_book -1]
            with open("books.txt" , "w") as rewrite:
                rewrite.writelines(lines)
            return
        else:
            print("This book checked out, you can't delete")
    else:
        print("There isn't a book!")
def check_book():
    c_lis =  dict()
    with open("students.txt", "r") as x:
        students = x.readlines()
    std_no = input("Enter your student number: ")
    cnt = 0
    for student in students:
        std = student.strip().split(",")
        if std[0] == std_no:
            print("Welcome " + std[1] + "!")
            cnt = 1
            break
    if cnt == 0:
        print("There isn't a student with the student number " + std_no)
        return check_book()
    for student in students:
        std = student.strip().split(",")
        c_lis[std[0]] = std[1:]
    lines = readline()
    for line in lines:
        print(str(cnt) + ")" + line)
        cnt = cnt + 1
    check = int(input("Enter the book number that you want to check out: "))
    if not 1 <= check <= len(lines):
        print("Please enter an acceptable value!")
        return
    book = lines[check - 1].strip().split(",")
    if book[-1] == " T":
        print("This book has already checked out!")
        return
    else:
        book[-1] = " T"
        c_lis[std_no].append(lines[check - 1])
        lines[check - 1] = ",".join(book) + "\n"
        with open("books.txt", "w") as rewrite:
            rewrite.writelines(lines)
        print("Book checked out")
        with open("students.txt", "w") as x:
            for key, values in c_lis.items():
                line = ",".join(values)
                if not line == "":
                    x.write(f"{key}" + "," + line + "\n")
        return

def student_books():
    with open("students.txt", "r") as x:
        lines = x.readlines()
    for line in lines:
        std = line.strip().split(",")
        if len(std) > 1:
            print(std[0] + std[1])
            if len(std) > 2:
                cbook = len(std) // 4
                for i in  range(0,cbook):
                    print(std[(2+(4*i)) :(6*(i+1))])
        print("-"*20)
    return 

def menu():
    while True:
        print("-"*15 + " Library Management System " + "-"*15)
        print("WELCOME \n1) Add Book \n2) Add Student \n3) Search Book By ISBN \n4) Search Book By Name \n5) List All Books \n6) List Checked Out Books \n7) Delete Book \n8) Check Out Book \n9) Student List(With Checked book) \n10) Quit")
        choice = input("Please enter an option (1-10):")
        if choice == "1":
            add_book()
        elif choice == "2":
            add_student()
        elif choice == "3":
            book_search_by_isbn()
        elif choice == "4":
            book_search_by_name()
        elif choice == "5":
            all_books()
        elif choice == "6":
            all_checked_books()
        elif choice == "7":
            delete_book()
        elif choice == "8":
            check_book()
        elif choice == "9":
            student_books()
        elif choice == "10":
            print("Exiting the program...")
            break
        else:
            print("Enter a valid number.")

menu()