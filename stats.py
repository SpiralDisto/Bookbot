def num_words(text_of_book):
    words = text_of_book.split()
    return (len(words))

def number_characters(characters):
    characters = characters.lower()
    counted = {}
    for character in characters:
        if character in counted:
            counted[character] += 1
        else:
            counted[character] = 1
    return counted

def sorted_chars(counted):
    char_dict = []
    for char, num in counted.items():
        if char.isalpha():
            char_dict.append({"char": char, "num": num})
    char_dict.sort(reverse=True, key=lambda item: item["num"])
    return char_dict