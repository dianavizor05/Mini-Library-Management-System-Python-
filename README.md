# Mini-Library-Management-System-Python-

A console-based library application written in Python 3. It allows managing book inventory, tracking loans, searching books with regular expressions, and saving data automatically in JSON format.

## Features
- **Book Management:** Add, list, and delete books with duplicate checks and live stock updates.
- **Search:** Find books by partial title or author using regular expressions (`re`).
- **Loans & Returns:** Borrow and return books for specific users without allowing duplicate loans.
- **Data Persistence:** Automatically loads and saves library state to `books.json`.

## Project Files
- `main.py` – main menu and program entry point
- `library.py` – core library logic
- `book.py` & `person.py` – `Book` and `Person` classes
- `exceptions.py` – custom exceptions
- `decorators.py` – custom decorators
- `books.json` – data storage

## Tech Stack
- Python 3 (OOP, custom exceptions, decorators, generators, regex, JSON)

## How to Run
1. Clone the repository:
   git clone https://github.com/dianavizor05/Mini-Library-Management-System-Python-.git
2. Navigate to the folder and run the app:
   cd Mini-Library-Management-System-Python-
   python main.py
