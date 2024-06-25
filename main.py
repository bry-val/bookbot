def main():
    path = "books/frankenstein.txt"
    book = read_book(path)
    # print(count_words(book))
    print_report(path)


def count_letters(book: str):
    chars = {}
    book = book.lower()
    for letter in book:
        chars[letter] = chars.get(letter, 0) + 1
    return chars


def count_words(book: str):
    return len(book.split())


def read_book(path: str):
    with open(file=path) as f:
        book = f.read()
    return book


def sort_on(word_dict: dict):
    return word_dict['count']


def char_dict_to_list(char_dict: dict):
    char_list = []
    for key, val in char_dict.items():
        if key.isalpha():
            char_list.append({'char': key, 'count': val})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def print_report(path: str):
    book = read_book(path)
    print(f"--- Begin report of {path} ---")
    print(f"{count_words(book)} words found in the document\n")
    for char_list in char_dict_to_list(count_letters(book)):
        print(f"The '{char_list['char']}' character was found {char_list['count']} times")
    print("--- End report ---")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
