from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text("books/frankenstein.txt")
    get_num_words(text)
    

main()