# Get file content
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

import sys
from stats import get_num_words
from stats import characters_count
from stats import dico

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    booktolook = sys.argv[1]
    book = get_book_text(booktolook)
    def main():
        
        character_count = characters_count(book)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {booktolook}")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(book)} total words")
        print("--------- Character Count -------")
        new_list = dico(character_count)
        for item in new_list:
            print(f"{item['char']}: {item['num']}")

    main()


