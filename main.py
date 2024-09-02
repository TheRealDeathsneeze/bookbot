# bookbot project for boot.dev by beccaKay

def main(): 
    #change to ask for input or pass as arg later
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    chars_dict = get_char_dict(text)
    print(f"word count: {word_count}")
    print(chars_dict)

#count independent characters and return a dictionary
def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] +=1
        else:
            chars[lowered] = 1
    return chars

#count number of words
def get_num_words(text):
    words = text.split()
    return len(words)


#open file and return contents
def get_book_text(path):
    with open(path) as f:
        return f.read()



main()


