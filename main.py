import sys
from stats import get_word_count, num_char, transform_sort


def get_book_text(filepath: str):
    with open(filepath) as f:
        text = f.read()
        return text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    result = get_book_text(book_path)
    total_word_count = get_word_count(result)
    char_data = num_char(result)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_word_count} total words")
    print("--------- Character Count -------")
    final_result = transform_sort(char_data)
    for ch in final_result:
        print(f"{ch['char']}: {ch['num']}")


main()
