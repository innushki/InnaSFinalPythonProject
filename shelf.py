class Shelf:
    def __init__(self):
        self.books = [None, None, None, None, None]
        self.isShelfFull = False

    def addBook(self, book):
        added = False
        for i in range(5):
            if self.books[i] == None:
                self.books[i] = book
                added = True
                break
        if added:
            full = True
            for b in self.books:
                if b == None:
                    full = False
            self.isShelfFull = full
        else:
            print("The shelf is full. Cannot add more books.")

    def replaceBooks(self, pozi1, pozi2):
        if pozi1 < 1 or pozi1 > 5 or pozi2 < 1 or pozi2 > 5:
            print("Positions must be between 1 and 5.")
            return
        if self.books[pozi1 - 1] == None or self.books[pozi2 - 1] == None:
            print("One of the positions is empty, cannot replace.")
            return
        temp = self.books[pozi1 - 1]
        self.books[pozi1 - 1] = self.books[pozi2 - 1]
        self.books[pozi2 - 1] = temp