import json
import re

from book import Book
from person import Person
from decorators import action_info
from exceptions import BookNotFoundError, BookAlreadyExistsError, NoCopiesError, PersonNotFoundError, BorrowError


class Library:
    def __init__(self):
        self.books = []
        self.people = []

    @action_info
    def add_book(self, title, author, year, copies):
        if title == "" or author == "":
            print("Tytuł i autor nie mogą być puste.")
            return

        if int(year) < 0 or int(copies) < 1:
            print("Rok nie może być ujemny, a liczba sztuk musi być większa od zera.")
            return

        existing_books = {(book.title.lower(), book.author.lower()) for book in self.books}
        new_book = (title.lower(), author.lower())

        if new_book in existing_books:
            raise BookAlreadyExistsError("Taka książka już istnieje w bibliotece.")

        book = Book(title, author, int(year), int(copies))
        self.books.append(book)
        print("Dodano książkę.")

    def show_books(self):
        if len(self.books) == 0:
            print("Brak książek.")
            return

        sorted_books = sorted(self.books, key=lambda book: book.title)

        for number, book in enumerate(sorted_books, start=1):
            print("-" * 80)
            print(f"{number}. {book}")

        print("-" * 80)

    def search_generator(self, pattern):
        for book in self.books:
            text = book.title + " " + book.author
            if re.search(pattern, text, re.IGNORECASE):
                yield book

    def search_books(self, pattern):
        results = [book for book in self.search_generator(pattern)]

        if len(results) == 0:
            raise BookNotFoundError("Nie znaleziono książki.")

        for book in results:
            print(book)

    @action_info
    def remove_book(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]

        if len(found_books) == 0:
            raise BookNotFoundError("Nie znaleziono książki do usunięcia.")

        self.books.remove(found_books[0])
        print("Usunięto książkę.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

        raise BookNotFoundError("Nie znaleziono książki.")

    def find_person(self, name):
        for person in self.people:
            if person.name.lower() == name.lower():
                return person

        raise PersonNotFoundError("Nie znaleziono osoby.")

    def get_or_create_person(self, name):
        people_names = {person.name.lower() for person in self.people}

        if name.lower() not in people_names:
            self.people.append(Person(name))

        return self.find_person(name)

    @action_info
    def borrow_book(self, title, person_name):
        book = self.find_book(title)

        if book.copies <= 0:
            raise NoCopiesError("Brak dostępnych sztuk tej książki.")

        person = self.get_or_create_person(person_name)

        if book.title in person.borrowed_books:
            raise BorrowError("Ta osoba już wypożyczyła tę książkę.")

        book.copies -= 1
        person.borrowed_books.append(book.title)

        print("Wypożyczono książkę.")

    @action_info
    def return_book(self, title, person_name):
        book = self.find_book(title)
        person = self.find_person(person_name)

        if book.title not in person.borrowed_books:
            raise BorrowError("Ta osoba nie ma wypożyczonej tej książki.")

        person.borrowed_books.remove(book.title)
        book.copies += 1

        print("Zwrócono książkę.")

    def show_people(self):
        people_with_books = [person for person in self.people if len(person.borrowed_books) > 0]

        if len(people_with_books) == 0:
            print("Nikt nie ma wypożyczonych książek.")
            return

        for person in people_with_books:
            print("-" * 80)
            print(person.name + ":")

            for book_title in person.borrowed_books:
                print("-", book_title)

        print("-" * 80)

    def save_to_file(self, filename):
        data = {
            "books": [book.to_dict() for book in self.books],
            "people": [person.to_dict() for person in self.people]
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("Zapisano dane do pliku.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.books = [Book.from_dict(item) for item in data["books"]]
            self.people = [Person.from_dict(item) for item in data["people"]]

            print("Wczytano dane z pliku.")

        except FileNotFoundError:
            print("Nie znaleziono pliku.")
        except json.JSONDecodeError:
            print("Plik JSON jest uszkodzony.")
        except KeyError:
            print("Plik JSON ma niepoprawną strukturę.")