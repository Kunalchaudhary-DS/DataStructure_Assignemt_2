# Library Management System (Python)

## Description
This is a **console-based Library Management System** developed in Python. It uses a **linked list** to store and manage books and a **stack** to track transactions, enabling users to issue, return, and undo operations efficiently. The system provides a simple and interactive interface to manage library operations while demonstrating **object-oriented programming (OOP)** concepts in Python.

---

## Features
- Add new books to the library with details like ID, title, and author.
- Delete books from the library using their ID.
- Search for books by ID and view their details (title, author, status).
- Issue books to users (updates book status to "Issued").
- Return books to the library (updates book status to "Available").
- Undo the last transaction (issue or return) using a stack.
- View a history of all recent transactions.
- Display all books with their current status in the library.

---

## How It Works
1. **Linked List for Book Storage:**  
   The library uses a linked list to store all book entries dynamically, allowing easy insertion and deletion without rearranging the entire dataset.

2. **Transaction Stack:**  
   Every issue or return action is pushed onto a stack. This allows the user to undo the most recent transaction by popping it from the stack and reversing its effect.

3. **Book Status Management:**  
   Each book has a `status` property (`Available` or `Issued`). Issuing a book changes its status to "Issued", returning a book changes it back to "Available".

4. **Menu-Driven Interface:**  
   Users interact with the system via a simple console menu to perform all operations in a guided manner.

---

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Library-Management-System-Python.git

---

## Example Run
 LIBRARY MANAGEMENT SYSTEM
1. Search Book
2. Insert Book
3. Delete Book
4. Issue Book
5. Return Book
6. Undo Last Transaction
7. View Transactions
8. Display All Books
9. Exit

Enter your choice: 2
Enter Book ID: 101
Enter Book Title: Python Programming
Enter Author Name: John Doe

Book 'Python Programming' is successfully added

Enter your choice: 4
Enter Book ID to issue: 101

Got a Book:
ID: 101
Title: Python Programming
Author: John Doe
Status: Available
Book 'Python Programming' issued successfully!

---

## Technologies Used
Python 3

Object-Oriented Programming (OOP)

Linked List (for dynamic book storage)

Stack (for transaction history)

Console-based user interface

---

## Learning Outcomes
Understand and implement linked lists for dynamic data storage.

Learn to use stack data structures for undo/redo operations.

Apply OOP concepts such as classes, objects, and methods.

Build an interactive console-based application with menu-driven input.

Manage real-world scenarios like book issuing, returning, and transaction history.
