def main():
    book_path = "/Users/brettburns/workspace/github.com/0xburnsy/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path).lower()
    words = get_words(text)   
    num_words = len(words)
    print(f"This book contains {num_words} words.")
    print(get_character_count(words))

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_words(text):
    return text.split()

def get_character_count(words):
    character_dictionary = {}
    for word in words:
        for character in word:
            if character in character_dictionary:
                character_dictionary[character] += 1
            else:
                character_dictionary[character] = 1
    return character_dictionary

if __name__ == "__main__":
    main()