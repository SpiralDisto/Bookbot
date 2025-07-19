import sys
from stats import num_words
from stats import number_characters
from stats import sorted_chars

def get_book_text(book):
    with open(book) as f:
        book_contents = f.read()
        return(book_contents)



def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    book_path = sys.argv[1]
    book = get_book_text(book_path)
    word_count = num_words(book)
    num_appeared = number_characters(book)
    sorted_dictionary = sorted_chars(num_appeared)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for item in sorted_dictionary:
        print(f"{item['char']}: {item['num']}")


    print("============= END ===============")

main()

