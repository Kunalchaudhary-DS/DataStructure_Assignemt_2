# Class representing a single book in the library
class BookLink:
    def __init__(self, book_id, title, author, status="Available"):
        """
        Create a new book node to store book details.
        Each book has:
        - book_id: unique identifier for the book
        - title: name of the book
        - author: author of the book
        - status: current availability ("Available" by default)
        - next: pointer to the next book in the linked list
        We use a linked list to allow easy insertion/deletion of books.
        """

        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
        self.next = None  

# Class managing the library books using a linked list
class BookList:
    def __init__(self):
        # Head of the linked list, initially None (empty library)
        self.Info = None

    def insertBook(self, book_id, title, author):
        """
        Insert a new book into the library.
        Logic:
        1. Create a new BookLink node.
        2. If the library is empty, make it the head.
        3. If not, traverse to the end and append it.
        This ensures books are stored in the order they were added.
        """

        NewBook = BookLink(book_id, title, author)

        if self.Info is None:
            self.Info = NewBook  # Library is empty, new book becomes head
        else:
            # Traversing to the last book
            temp = self.Info
            while temp.next:
                temp = temp.next
            # Appending the new book at the end
            temp.next = NewBook

        print(f"\nBook '{title}' is successfully added")

    def deleteBook(self, book_id):
        """
        Delete a book from the library using its book_id.
        Logic:
        1. Traverse the list to find the book.
        2. Keep track of previous node to update its 'next' pointer.
        3. If book is head, update head pointer.
        4. Else, bypass the book to remove it from the list.
        """

        temp = self.Info
        previous = None

        while temp and temp.book_id != book_id:
            previous = temp
            temp = temp.next

        if not temp:
            # Book not found
            print("No Book found!")
            return

        if previous:
            # Book is in middle or end, skip it
            previous.next = temp.next
        else:
            # Book is head, update head
            self.Info = temp.next

        print(f"Book '{temp.title}' is successfully deleted!")

    def searchBook(self, book_id):
        """
        Search for a book by its ID.
        Logic:
        1. Traverse linked list from head.
        2. If book_id matches, return the book node.
        3. If not found, return None.
        Useful for issuing/returning books or displaying details.
        """

        temp = self.Info

        while temp:
            if temp.book_id == book_id:
                # Found the book, display details
                print(f"\nGot a Book:\n"
                      f"ID: {temp.book_id}\nTitle: {temp.title}\nAuthor: {temp.author}\nStatus: {temp.status}")
                return temp
            temp = temp.next

        print("No Book found!")
        return None

    def displayBooks(self):
        """
        Display all books in the library.
        Logic:
        1. If library is empty, inform user.
        2. Else, traverse linked list and print details of each book.
        Useful to get an overview of current library stock.
        """

        if self.Info is None:
            print("\nLibrary is Empty!")
            return
        
        print("\nCurrent Library Stock:")
        print("------------------------------------")
        temp = self.Info

        while temp:
            print(f"ID: {temp.book_id} | Title: {temp.title} | Author: {temp.author} | Status: {temp.status}")
            temp = temp.next


# Class to manage transactions for undo functionality
class TransactionStack:
    def __init__(self):
        # Stack implemented using a Python list
        # Each transaction is a dictionary containing 'BookID' and 'Perform' (Issue/Return)
        self.stack = []

    def push(self, transaction):
        """
        Push a transaction onto the stack.
        Logic:
        1. Store both book ID and action performed.
        2. Allows undoing this exact transaction later.
        """

        self.stack.append(transaction)

    def pop(self):
        """
        Remove and return the last transaction.
        Logic:
        1. If stack is empty, there’s nothing to undo.
        2. Otherwise, pop the last action to reverse it.
        """

        if not self.stack:
            print("\nNo transaction to undo!")
            return None
        return self.stack.pop()

    def viewTransactions(self):
        """
        Display all transactions in reverse order (latest first).
        Useful to check history of issued/returned books.
        """

        if not self.stack:
            print("\nNo transactions are found yet!")
            return
        
        print("\nLatest Transactions:")
        for i in reversed(self.stack):
            print(f"{i['Perform']} Book ID: {i['BookID']}")


# Class to manage issuing, returning, and undoing books
class LibraryManagement:
    def __init__(self):
        # Initializing book list and transaction stack
        self.book_list = BookList()
        self.transaction_stack = TransactionStack()

    def issueBook(self, book_id):
        """
        Issue a book if it is available.
        Logic:
        1. Search for the book using book_id.
        2. If found and status is 'Available', mark it as 'Issued'.
        3. Push the transaction onto the stack for undo.
        4. If already issued, inform user.
        """

        book = self.book_list.searchBook(book_id)

        if book and book.status == "Available":
            book.status = "Issued"
            self.transaction_stack.push({"BookID": book_id, "Perform": "Issue"})
            print(f"Book '{book.title}' issued successfully!")
        elif book:
            print("Book already issued!")

    def returnBook(self, book_id):
        """
        Return a book if it is currently issued.
        Logic:
        1. Search for the book using book_id.
        2. If found and status is 'Issued', mark it as 'Available'.
        3. Push transaction onto the stack for undo.
        4. If already available, inform user.
        """

        book = self.book_list.searchBook(book_id)

        if book and book.status == "Issued":
            book.status = "Available"
            self.transaction_stack.push({"BookID": book_id, "Perform": "Return"})
            print(f"Book '{book.title}' is successfully returned!")
        elif book:
            print("Book is already available!")

    def undoTransaction(self):
        """
        Undo the last transaction (Issue or Return).
        Logic:
        1. Pop the last transaction from stack.
        2. Search for the book involved in transaction.
        3. Reverse the status (Issued -> Available, Available -> Issued)
        4. Inform user of successful undo.
        """

        last = self.transaction_stack.pop()

        if not last:
            return

        book = self.book_list.searchBook(last["BookID"])
        if not book:
            return
        
        # Reversing the action
        if last["Perform"] == "Issue":
            book.status = "Available"
            print(f"Undo Successful: Book '{book.title}' marked as Available again.")
        elif last["Perform"] == "Return":
            book.status = "Issued"
            print(f"Undo Successful: Book '{book.title}' marked as Issued again.")

# Main function to perform the Backend
def main():
    """
    Main interactive menu for Library Management System.
    Logic:
    1. Initialize LibraryManagement object.
    2. Display menu repeatedly until user exits.
    3. Take user input and perform corresponding action.
    4. Handles searching, inserting, deleting, issuing, returning, undoing, viewing transactions, and displaying all books.
    """
    
    library = LibraryManagement()

    while True:
        # Menu options for user
        print("\n LIBRARY MANAGEMENT SYSTEM ")
        print("1. Search Book")
        print("2. Insert Book")
        print("3. Delete Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Undo Last Transaction")
        print("7. View Transactions")
        print("8. Display All Books")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        # Execute the chosen operation
        if choice == "1":
            book_Id = int(input("Enter Book ID to search: "))
            library.book_list.searchBook(book_Id)

        elif choice == "2":
            book_Id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            library.book_list.insertBook(book_Id, title, author)

        elif choice == "3":
            book_Id = int(input("Enter Book ID to delete: "))
            library.book_list.deleteBook(book_Id)

        elif choice == "4":
            book_Id = int(input("Enter Book ID to issue: "))
            library.issueBook(book_Id)

        elif choice == "5":
            book_Id = int(input("Enter Book ID to return: "))
            library.returnBook(book_Id)

        elif choice == "6":
            library.undoTransaction()

        elif choice == "7":
            library.transaction_stack.viewTransactions()

        elif choice == "8":
            library.book_list.displayBooks()

        elif choice == "9":
            print("\nExiting Library System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter again.")


# Entry point for program execution
if __name__ == "__main__":
    main()
