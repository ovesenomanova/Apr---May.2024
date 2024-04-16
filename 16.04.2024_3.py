class Library:
    def __init__(self, name, address, book_account):
        self.name = name
        self.address = address
        self.book_account = book_account

    def __add__(self, other):
        if type(other) == int:
            return Library(self.name, self.address, self.book_account + other)
        if type(other) == Library:
            return Library(self.name, self.address, self.book_account + other.book_account)

    def __sub__(self, other):
        if type(other) == int:
            return Library(self.name, self.address, self.book_account - other)
        if type(other) == Library:
            return Library(self.name, self.address, self.book_account - other.book_account)

    def __lt__(self, other):
        if type(other) == int:
            return self.book_account < other
        if type(other) == Library:
            return self.book_account < other.book_account

    def __gt__(self, other):
        if type(other) == int:
            return self.book_account > other
        if type(other) == Library:
            return self.book_account > other.book_account

    def __le__(self, other):
        if type(other) == int:
            return self.book_account <= other
        if type(other) == Library:
            return self.book_account <= other.book_account

    def __ge__(self, other):
        if type(other) == int:
            return self.book_account >= other
        if type(other) == Library:
            return self.book_account >= other.book_account

    def __eq__(self, other):
        if type(other) == int:
            return self.book_account == other
        if type(other) == Library:
            return self.book_account == other.book_account

    def __ne__(self, other):
        if type(other) == int:
            return self.book_account != other
        if type(other) == Library:
            return self.book_account != other.book_account
