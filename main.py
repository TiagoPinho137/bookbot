import string


class Book:
    def __init__(self, book):
        self.book = book

    def open_book(self):
        with open(self.book, "r") as b:
            read_content = b.read()
        return read_content


class Counters(Book):
    def __init__(self, book):
        super().__init__(book)

    def cont_words(self):
        words = self.open_book().split()
        return len(words)

    def cont_letters(self):
        words = dict.fromkeys(string.ascii_lowercase, 0)
        count = 0
        for char in self.open_book().lower():
            count += 1
            if char in words:
                words[char] += 1

        for char in words:
            print(f"the character '{char}' was found '{words[char]}' times")
        return count


def main(book_extension):
    ob = Book(book_extension)
    print(ob.open_book(), "\n")

    cl = Counters(book_extension)
    print(f"--- Begin of the report of {book_extension} ---")
    print(f"{cl.cont_words()} words found in the document", "\n")
    print(f"There are {cl.cont_letters()} Characters", "\n")
    print("--- End of the Report ---")


main("books/frankenstein.txt")
