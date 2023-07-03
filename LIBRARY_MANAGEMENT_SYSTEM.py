import csv

def add_book(book_name, serial_number):
    # Open the books CSV file for writing
    with open('books.csv', mode='a', newline='') as file:
        # Create a writer object
        writer = csv.writer(file)
        # Write the book's information
        writer.writerow([book_name, serial_number, 0])
    return "Book added successfully!"

def add_user(name, email, phone_number):
    # Open a file for writing
    with open('users.csv', mode='a', newline='') as file:
        # Create a writer object
        writer = csv.writer(file)
        # Write the user's information
        writer.writerow([name, email, phone_number])
    return "User added successfully!"
def rent_book(book_serial, email, cost_per_day, days_of_rent):
    book_rented = False
    with open('books.csv', 'r') as file:
        reader = csv.reader(file)
        books = list(reader)
        for index, book in enumerate(books):
            if book[1] == book_serial:
                if int(book[2]) == 0:
                    book[2] = 1
                    book_rented = True
                    break
                else:
                    print("Book already rented.")
                    return
    with open('books.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(books)
    if book_rented:
        with open('users.csv', 'r') as file:
            reader = csv.reader(file)
            users = list(reader)
            for user in users:
                if user[1] == email:
                    user.append([book_serial, cost_per_day, days_of_rent])
                    break
        with open('users.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(users)
        print("Book rented successfully!")
    else:
        print("Book not found.")

while True:
    print("Please select an option:")
    print("[1] Add a book")
    print("[2] Add a user")
    print("[3] Rent a book")
    print("[4] Return a book")
    print("[5] Delete a book")
    print("[6] Delete a user")
    print("[7] Exit")
    choice = int(input())
    if choice not in range(1,8):
        print("Invalid entry")
    else:
        if choice == 1:
            book_name = input("Enter the name of the book: ")
            book_serial = input("Enter the serial number of the book: ")
            print(add_book(book_name, book_serial))
        elif choice == 2:
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            phone_number = input("Enter user phone number: ")
            print(add_user(name, email, phone_number))
        elif choice == 3:
            # Rent a book code here
            book_serial = input("Enter the serial number of the book: ")
            email = input("Enter the email of the user: ")
            cost_per_day = input("Enter the cost per day of the book: ")
            days_of_rent = input("Enter the number of days the book will be rented for: ")
            rent_book(book_serial, email, cost_per_day, days_of_rent)

        elif choice == 4:
            book_returned = False
            # Get the serial number of the book being returned
            book_serial = input("Enter the serial number of the book being returned: ")
            # Open the books.csv file
            with open('books.csv', 'r') as file:
                reader = csv.reader(file)
                books = list(reader)
                # Iterate through the books and check if the book being returned is found
                for index, book in enumerate(books):
                    if book[1] == book_serial:
                        if int(book[2]) == 1:
                            # If the book is found and is currently rented, change its status to available
                            book[2] = 0
                            book_returned = True
                            break
                        else:
                            print("Book is not currently rented.")
                            #return
            # Write the updated information to the books.csv file
            with open('books.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(books)
            if book_returned:
                # Open the users.csv file
                with open('users.csv', 'r') as file:
                    reader = csv.reader(file)
                    users = list(reader)
                    # Iterate through the users and find the user who rented the book
                    for user in users:
                        if user == email:
                            # Remove the book's information from the user's rented books
                            user.remove([book_serial, cost_per_day, days_of_rent])
                            break
                # Write the updated information to the users.csv file
                with open('users.csv', 'w') as file:
                    writer = csv.writer(file)
                    writer.writerows(users)
                print("Book returned successfully!")
            else:
                print("Book not found.")
        elif choice == 5:
            book_deleted = False
            # Get the serial number of the book being deleted
            book_serial = input("Enter the serial number of the book being deleted: ")
            # Open the books.csv file
            with open('books.csv', 'r') as file:
                reader = csv.reader(file)
                books = list(reader)
                # Iterate through the books and check if the book being deleted is found
                for index, book in enumerate(books):
                    if book[1] == book_serial:
                        if int(book[2]) == 0:
                            # If the book is found and is currently available, delete it from the list
                            del books[index]
                            book_deleted = True
                            break
                        else:
                            print("Book is currently rented and can't be deleted.")
                            #return
            # Write the updated information to the books.csv file
            with open('books.csv', 'w') as file:
                writer = csv.writer(file)
                writer.writerows(books)
            if book_deleted:
                print("Book deleted successfully!")
            else:
                print("Book not found.")
        elif choice == 6:
            # Delete a user code here
            pass
        elif choice == 7:
            break
        else:
            print("Invalid choice, please select a valid option.")
    a = input("Do you want to make another entry? (yes/no): ")
    if a.lower() == "no":
        break
    else:
        continue
