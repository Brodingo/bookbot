def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    lowered_string = text.lower()
    chars = {}

    for char in lowered_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

main()
