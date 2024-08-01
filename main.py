def main():
    book_path = "/Users/brettburns/workspace/github.com/0xburnsy/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_word_count(text))

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

if __name__ == "__main__":
    main()