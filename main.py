# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    path = "books/frankenstein.txt"
    book = read_book(path)
    print(count_words(book))


def count_words(book):
    return len(book.split())


def read_book(path):
    with open(file=path) as f:
        book = f.read()
    return book


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
