def display_menu():
    print("Library Management System")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Borrowed Books")
    print("6. Exit")

def load_data(file):
    with open(file, 'r') as f:
        return f.readlines()

def save_data(file, data):
    with open(file, 'w') as f:
        f.writelines(data)

def add_book():
    books = load_data('books.txt')
    book_id = len(books)
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter year published: ")
    books.append(f"{book_id},{title},{author},{year},Yes\n")
    save_data('books.txt', books)
    print("Book added successfully.")

def view_books():
    books = load_data('books.txt')
    for book in books:
        print(book.strip())

def borrow_book():
    books = load_data('books.txt')
    borrowed_books = load_data('borrowed_books.txt')
    users = load_data('users.txt')

    user_id = input("Enter your user ID: ")
    user = next((u for u in users if u.startswith(user_id)), None)
    if not user:
        print("User not found.")
        return

    book_id = input("Enter the book ID to borrow: ")
    book = next((b for b in books if b.startswith(book_id)), None)
    if not book or book.split(',')[4].strip() == 'No':
        print("Book not available.")
        return

    books = [b.replace(f"{book_id},", f"{book_id},") if b.startswith(book_id) else b for b in books]
    borrowed_books.append(f"{book_id},{user.split(',')[1].strip()},{book.split(',')[1].strip()},{date.today()}\n")
    save_data('books.txt', books)
    save_data('borrowed_books.txt', borrowed_books)
    print("Book borrowed successfully.")

def return_book():
    books = load_data('books.txt')
    borrowed_books = load_data('borrowed_books.txt')

    book_id = input("Enter the book ID to return: ")
    borrowed_book = next((b for b in borrowed_books if b.startswith(book_id)), None)
    if not borrowed_book:
        print("Book not found.")
        return

    books = [b.replace(f"{book_id},", f"{book_id},") if b.startswith(book_id) else b for b in books]
    borrowed_books = [b for b in borrowed_books if not b.startswith(book_id)]
    save_data('books.txt', books)
    save_data('borrowed_books.txt', borrowed_books)
    print("Book returned successfully.")

def view_borrowed_books():
    borrowed_books = load_data('borrowed_books.txt')
    for book in borrowed_books:
        print(book.strip())

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            borrow_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            view_borrowed_books()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
