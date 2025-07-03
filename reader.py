class Reader:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def readBook(self, title):
        self.books.append(title)
