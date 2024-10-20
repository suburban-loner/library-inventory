# Importing the sqlite3 module.
import sqlite3

# This is creating a connection to the database and creating a cursor to the database.
db = sqlite3.connect('ebookstore')
cursor = db.cursor()

# This is creating a table in the database called books.
cursor.execute('''create table if not exists books(id TEXT PRIMARY KEY, Title TEXT, Author TEXT, Qty INTEGER)''')
db.commit()

# This is creating a list of books that will be added to the database.
book_list = [('3001', 'A Tale of Two Cities', 'Charles Dickens', 30),
             ('3002', "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
             ('3003', 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
             ('3004', 'The Lord of the Rings', 'J.R.R Tolkien', 37), ('3005', 'Alice in Wonderland', 'Lewis Carroll', 12),
             ('3006', 'The Catcher in the Rye', 'J. D. Salinger', 20), ('3007', 'To Kill a Mockingbird', 'Harper Lee', 15),
             ('3008', 'The Great Gatsby', 'F. Scott Fitzgerald', 35), ('3009', 'Lord of the Flies', 'William Golding', 18)]
# This is inserting the book_list into the database.
cursor.executemany('''insert or replace into books(id, Title, Author, Qty) values(?,?,?,?)''', book_list)
db.commit()

# This is creating a loop that will keep the program running until the user selects 0 to exit the program.
while True:
    # This is creating a menu for the user to select what they would like to do.
    menu = input("Select one of the following:\n1 - Enter book\n2 - Update book\n3 - Delete book\n4 - Search book\n0 "
                 "- Exit\nSelection: ")

    if menu == '1':
        # This is asking the user to enter the title, author, and quantity of the book they would like to add to the
        # database.
        title = input("Enter the tile of the book: ")
        author = input("Enter the Author of the book: ")
        qty = int(input("Enter the quantity of the book: "))

        # This is inserting the title, author, and quantity of the book into the database.
        cursor.execute('''insert into books(Title, Author, Qty) values(?,?,?)''', (title, author, qty))
        db.commit()

        print("New book entered.\n")

    elif menu == '2':
        # This is asking the user to enter the title of the book they would like to update. Then it is creating
        # variables that will be used to store the information of the book that the user is searching for.
        search = input("What book would you like to update?: ")
        book_id = ''
        book_name = ''
        book_author = ''
        book_qty = 0

        # This is searching the book_list for the book that the user is searching for.
        for book in book_list:
            if book[1] == search:
                print("Book found!!\n")
                book_id = book[0]
                book_name = book[1]
                book_author = book[2]
                book_qty = book[3]

        # This is asking the user what they would like to update about the book they are searching for.
        update = input("what would you like to update:\ni - book id\nt - book title\na - book author\nq - book "
                       "quantity\nSelection: ")

        if update == 'i':
            # This is asking the user to enter the new book id that they would like to update the book with.
            info = input("Enter new book id: ")
            # This is updating the book id of the book that the user is searching for.
            cursor.execute('''update books set id = ? where Title = ?''', (info, book_name))
            db.commit()
            print("Book id updated!\n")

        elif update == 't':
            # This is asking the user to enter the new book title that they would like to update the book with.
            info = input("Enter new book title: ")
            # This is updating the book title of the book that the user is searching for.
            cursor.execute('''update books set Title = ? where id = ?''', (info, book_id))
            db.commit()
            print("Book title updated!\n")

        elif update == 'a':
            # This is asking the user to enter the new book author that they would like to update the book with.
            info = input("Enter new book author: ")
            # This is updating the book author of the book that the user is searching for.
            cursor.execute('''update books set Author = ? where Title = ?''', (info, book_name))
            db.commit()
            print("Book author updated!\n")

        elif update == 'q':
            # This is asking the user to enter the new book quantity that they would like to update the book with.
            info = int(input("Enter new book quantity: "))
            # This is updating the quantity of the book that the user is searching for.
            cursor.execute('''update books set Qty = ? where Title = ?''', (info, book_name))
            db.commit()
            print("Book quantity updated!\n")

    elif menu == '3':
        # This is asking the user to enter the title of the book that they would like to delete.
        title = input("What book would you like to delete?: ")

        # This is deleting the book that the user is searching for.
        cursor.execute('''delete from books where Title = ?''', (title, ))
        db.commit()
        print("Book deleted!\n")

    elif menu == '4':
        # This is asking the user to enter the title of the book that they are searching for. Then it is creating a
        # variable that will be used to store the title of the book that the user is searching for.
        search = input("What is the title for the book you are searching for?: ")
        book_name = ''

        # This is searching the book_list for the book that the user is searching for.
        for book in book_list:
            if book[1] == search:
                book_name = book[1]
                print("Book found!!\n")

        # This is selecting the id, title, author, and quantity of the book that the user is searching for. Then it
        # is fetching the information of the book that the user is searching for. Then it is committing the changes
        # to the database. Then it is printing the information of the book that the user is searching for.
        cursor.execute('''select id, Title, Author, Qty from books where Title = ?''', (book_name, ))
        book1 = cursor.fetchone()
        db.commit()
        print(book1)
        print(" ")

    elif menu == '0':
        print("Goodbye!!!")
        # The exit() function is exiting the program.
        exit()

    else:
        print("Invalid Entry!!!")
