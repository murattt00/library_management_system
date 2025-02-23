Important Note!
Before running the code, make sure all required files( books.txt, students.txt and My_Library.py) are in the same location.
Otherwise, code doesn't run.
Below is how each function runs and what it does.
------
readline() function:
This function is opening books.txt in read mode("r").
Then reads each line and adds them in the lines variable.
Each lines contain a book ISBN, name and author.
------
add_book() function:
This function is opening books.txt in append("a") mode.
It takes ISBN, book and author name from user and add them in new_book variable.
In final, it appends the new_book to books.txt with write operation.
------
add_student() function:
It is just running like add_book function.
------
book_search_by_isbn() function:
Firstly it takes an ISBN nubmer from user.
Then reads lines with readline function.
With for loop, it splits each line as a list with comma.
And checks the ISBN took from user and first( I mean [0]) value of list(The ISBN number).
If are they equal it prints this line and breaks.
And if none of them equal to input it print this book does not exist.
In final, it asks if you want to search again with basic if blok.
------
book_search_by_name() function:
It is running like search_by_isbn_function but this time it takes a name from user.
In for loop, it checks for secant value of list witch is name.
And it prints all books included user input.
------
all_books() function:
It reads lines in books.txt with readline function.
Then with for loop and a counter it prints each book.
______
all_checked_books() function:
It reads lines in books.txt with readline function.
With for loop, it splits each line as a list with comma.
Then with if blok it checks the last value of list.(T or F)
If it is T(it means this book checked out) it prints the book.
------
delete_book() function:
It reads lines in books.txt with readline function.
Then with for loop it enumerate each line and prints them.
It takes a number(enumerated book number) from user and convert it to integer.
It controls the book if exist (continue to next step) or not(give a massage)
After ıt controls ıf the book checked out(give a massage) or not(continue).
If there isn't any problem it deletes the selected line.
It is opening books.txt in write mode("w") and with writeline commend it writes remaining books.
------
check_book() function:
First create a variable(c_list) as an empty dictionary.
It opens and reads students.txt like in other function.Each line contain a student.
Then it takes a student number from user(input).
In for loop, ıt create a list with split(",") commend  and check the
student number equal(break the loop and continue) or not(give massage).(if blok)
with another for loop converts each line to a list with split(",").
After it takes first element of list as a key and others as a value.(c_lis[std[0]] = std[1:])
It reads books.txt with readline commend and assign values in lines variable.
In for loop it enumerate each line and prints them.
Ask user for an enumerated book.(input)
Checking if users input is exist or not.
Splits selected line to a list and assign book variable.(split(","))
Checking if the book checked out or not.
Then it change the "F"(not checked  out) as "T"(checked out).
Appends the book variable to c_list student number key.
It opens books.txt and rewrite each line.
In final opens the students.txt and write a key(student number) and its value(student name and checked book) in each line.
 ------
student_books() function:
It is opening books.txt and reads each line with readline commend.
Then with for loop convert each line to a list with split commend.(std)
It checks if this student checked a book.
It prints first and second element of the list which is student number and student name.
After ıt checks if this student checked out any book.
If it checked  in for loop it prints each book's ısbn, name, author and checked ıcon(" T").
------
menu() function:
It is the heart's of this program.
In while true loop it prints all option user can do.
It asks user to and operation. (input)
With a basic if blok it call required function.
And functions do your selected operation.






