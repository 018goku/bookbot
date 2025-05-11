import sys
from stats import number_words
from stats import count_char
from stats import print_dic

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_book}")
    print("----------- Word Count ----------")
    number_words(path_book)
    print("--------- Character Count -------")
    r = count_char(path_book)
    print_dic(r)
    print("============= END ===============")

main()
