class Book:
    all = []  # List to store all Book instances
    
    def __init__(self, title):
        self._title = title
        Book.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            raise Exception("Title must be a string")
    
    def contracts(self):
        """Return a list of all contracts involving this book."""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Return a list of all authors associated with this book."""
        return [contract.author for contract in self.contracts()]



class Author:
    all = []  # List to store all Author instances
    
    def __init__(self, name):
        self._name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise Exception("Name must be a string")
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        if isinstance(book, Book):
            contract = Contract(author=self, book=book, date=date, royalties=royalties)
            return contract
        else:
            raise Exception("Book must be an instance of the Book class")
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []  # List to store all Contract instances
    
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)
        else:
            raise Exception("Author must be an Author instance and book must be a Book instance")
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("Date must be a string")
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception("Royalties must be an integer")
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
