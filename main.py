import stats
import sys

def get_book_text(file_path):
    with open(file_path) as book:
        print(f"Analyzing book found at {file_path}...")
        return book.read()

if __name__ == "__main__":  
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])
    word_count = stats.count_words(book_text)
    character_counts = stats.character_count(book_text)
    sorted = stats.dictionary_sorter(character_counts)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    for char, count in sorted.items():
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    
    print("============= END ===============")