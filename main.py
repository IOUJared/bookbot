
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_string = text_as_string(text)
    sorted_dict = sort_on(char_string)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for i in sorted_dict:
        if i[0].isalpha():
            print(f"The '{i[0]}' character was found {i[1]} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def text_as_string(text):
    char_list = {}
    counter = 0
    lower_text = text.lower()
    for t in lower_text:
        if t in char_list:
            char_list[t] += 1
        else:
            char_list[t] = 1
    return char_list
             
def sort_on(d):
    sorted_dict = sorted(d.items(), key=lambda x:x[1], reverse=True)
    return sorted_dict



    
main()