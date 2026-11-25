class BookNotFoundError(Exception):
    pass


class BookAlreadyExistsError(Exception):
    pass


class NoCopiesError(Exception):
    pass


class PersonNotFoundError(Exception):
    pass


class BorrowError(Exception):
    pass