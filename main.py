from library import Library
from exceptions import BookNotFoundError, BookAlreadyExistsError, NoCopiesError, PersonNotFoundError, BorrowError


def show_menu():
    print()
    print("=== MINI BIBLIOTEKA ===")
    print("1. Dodaj książkę")
    print("2. Pokaż książki")
    print("3. Wyszukaj książkę")
    print("4. Usuń książkę")
    print("5. Wypożycz książkę")
    print("6. Zwróć książkę")
    print("7. Pokaż osoby i wypożyczone książki")
    print("0. Wyjście")


def main():
    library = Library()
    filename = "books.json"

    library.load_from_file(filename)

    while True:
        show_menu()
        choice = input("Wybierz opcję: ")

        try:
            if choice == "1":
                title = input("Podaj tytuł: ")
                author = input("Podaj autora: ")
                year = input("Podaj rok wydania: ")
                copies = input("Podaj liczbę sztuk: ")

                if year.isdigit() and copies.isdigit():
                    library.add_book(title, author, year, copies)
                else:
                    print("Rok i liczba sztuk muszą być liczbami.")

            elif choice == "2":
                library.show_books()

            elif choice == "3":
                pattern = input("Podaj szukaną frazę: ")
                library.search_books(pattern)

            elif choice == "4":
                title = input("Podaj tytuł książki do usunięcia: ")
                library.remove_book(title)

            elif choice == "5":
                title = input("Podaj tytuł książki: ")
                person_name = input("Podaj imię i nazwisko osoby: ")
                library.borrow_book(title, person_name)

            elif choice == "6":
                title = input("Podaj tytuł książki: ")
                person_name = input("Podaj imię i nazwisko osoby: ")
                library.return_book(title, person_name)

            elif choice == "7":
                library.show_people()

            elif choice == "0":
                library.save_to_file(filename)
                print("Koniec programu.")
                break

            else:
                print("Nie ma takiej opcji.")

        except BookNotFoundError as error:
            print(error)
        except BookAlreadyExistsError as error:
            print(error)
        except NoCopiesError as error:
            print(error)
        except PersonNotFoundError as error:
            print(error)
        except BorrowError as error:
            print(error)


main()