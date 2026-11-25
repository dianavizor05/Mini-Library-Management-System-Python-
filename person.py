class Person:
    def __init__(self, name, borrowed_books=None):
        self.name = name

        if borrowed_books is None:
            self.borrowed_books = []
        else:
            self.borrowed_books = borrowed_books

    def to_dict(self):
        return {
            "name": self.name,
            "borrowed_books": self.borrowed_books
        }

    @staticmethod
    def from_dict(data):
        return Person(data["name"], data["borrowed_books"])

    def __str__(self):
        return self.name