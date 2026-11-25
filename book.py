class Book:
    def __init__(self, title, author, year, copies):
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "copies": self.copies
        }

    @staticmethod
    def from_dict(data):
        return Book(data["title"], data["author"], data["year"], data["copies"])

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year}), dostępne sztuki: {self.copies}"