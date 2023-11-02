def num_of_words(book):
    words = book.split()
    return len(words)

def num_of_letter(book):
    book = book.lower()
    letters_count = {}
    for letter in book:
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 0
    return letters_count

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = num_of_words(file_contents)
    letter_counts = num_of_letter(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print("")
    letter_list = []
    for character in letter_counts:
        if character.isalpha():
            letter_list.append((letter_counts[character],character))
    letter_list.sort(reverse=True)
    for count, letter  in letter_list:
        print(f"The {letter} character was found {count} times")
    print("--- End report ---")

