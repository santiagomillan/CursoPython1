class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"Sorry, '{self.title}' is currently not available")
    
    def return_book(self):
        self.available = True
        print(f"You have returned '{self.title}'")

class User: 
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry, '{book.title}' is currently not available")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"You did not borrow '{book.title}'")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library")

    def register_user(self, user):
        self.users.append(user)
        print(f"Registered user '{user.name}'")

    def show_available_books(self):
        print("Available books:")
        for book in self.books:
            if book.available:
                print(f"- {book.title} by {book.author}")

# Example usage
#Crear los libros
book1 = Book("El principito", "Antoine de Saint-ExupÃ©ry")
book2 = Book("1984", "George Orwell")

#Crear usuario
user1 = User("Carli", "001")

#Crear Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

#Mostrar libros
library.show_available_books()

#Realizar prestamo
user1.borrow_book(book1)

#Mostrar libros
library.show_available_books()

#Devolver libro
user1.return_book(book1)

#Mostrar libros
library.show_available_books()