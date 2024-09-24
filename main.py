def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_chars(text)
    char_list = char_dict_list(char_count)
    char_list.sort(reverse=True,key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char in char_list:
        print(f"The '{char['name']}' character was found {char['num']} times")
    print("--- End report ---")

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

def char_dict_list(dict):
    dict_list = []
    for char in dict:
        if char.isalpha():
            dict_list.append({"name":char,"num":dict[char]})
    return dict_list

def sort_on(dict):
    return dict["num"]

main()
