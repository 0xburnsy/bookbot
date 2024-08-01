def main():
    book_path = "/Users/brettburns/workspace/github.com/0xburnsy/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path).lower()
    words = get_words(text)
    dictionary = get_character_count(words)
    list_of_dictionaries = create_dictionary_list(dictionary)
    sorted_list = sort_dictionary_list(list_of_dictionaries)   
    num_words = len(words)

    print(f"--- Begin Report of {book_path} ---")
    print(f"{num_words} words in the documnet\n")
    for item in sorted_list:
        print(f"The '{item['character']}' character appears {item['count']} times")
    print(f"\n--- End Report ---")

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

def create_dictionary_list(dictionary):
    list_of_dictionaries = []
    for key, value in dictionary.items():
        new_dict = {"character": key, "count": value}
        list_of_dictionaries.append(new_dict)
    return list_of_dictionaries

def get_count(dictionary):
    return dictionary["count"]

def sort_dictionary_list(list_of_dictionaries):
    list_of_dictionaries.sort(key=get_count, reverse=True)
    return list_of_dictionaries

if __name__ == "__main__":
    main()