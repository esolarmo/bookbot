from stats import get_num_words
from stats import get_num_chars
from stats import sorted_counts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main(path_to_book):
    text = get_book_text(path_to_book)
    wordcount = get_num_words(text)

    char_counts = get_num_chars(text)
    sorted = sorted_counts(char_counts)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for s in sorted:
        if s["char"].isalpha() == True:
            print(f"{s["char"]}: {s["num"]}")
    print("============= END ===============")

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])