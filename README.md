## Library Management System

### Description
A simple Library Management System built using Python. This system allows for adding, viewing, borrowing, and returning books. Data is stored in text files.

### Features
1. **Book Management**:
   - Add new books.
   - View all books.

2. **Borrowing and Returning Books**:
   - Borrow books.
   - Return books.
   - View borrowed books.

### Project Structure
```
library_management/
├── app.py
├── books.txt
├── borrowed_books.txt
└── users.txt
```

### Usage
1. Navigate to the project directory:
   ```bash
   cd library_management
   ```

2. Run the program:
   ```bash
   python app.py
   ```

3. Follow the on-screen instructions.

### Example Data
- **`books.txt`**:
  ```
  ID,Title,Author,Year,Available
  1,1984,George Orwell,1949,Yes
  2,To Kill a Mockingbird,Harper Lee,1960,Yes
  ```

- **`borrowed_books.txt`**:
  ```
  ID,User,Title,Date Borrowed
  ```

- **`users.txt`**:
  ```
  ID,Name
  1,John Doe
  2,Jane Smith
  ```

### License
This project is licensed under the MIT License.
