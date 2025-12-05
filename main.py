from stats import count_words, count_characters, sort_character_counts
import sys 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_of_words = count_words(text)
    count_list = sort_character_counts(count_characters(text))
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at  {book_path}.")
    print("---------- Word Count -----------")
    print(f"Found {num_of_words} total words")
    print("-------- Character Count --------")
    
    for x in count_list:
        if x[0].isalpha():
            print(f"{x[0]}: {x[1]}")


if __name__ == "__main__":
    main()
