# bookbot project for boot.dev by beccaKay
#  
def main(): 
    #change to ask for input or pass as arg later
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    chars_dict = get_char_dict(text)
    
    
    #print(text) if query("Read Book Text?") == True else None
    #print(f"word count: {word_count}") if query("Word count?") == True else None
    #print(chars_dict) if query("Character dictionary?") == True else None

    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

############################################################
# Main Functionality of bookbot goes here
############################################################

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

# prompt user for Y/n input, return true if Y
# any input other than 'y' returns false
# keeping it simple for now. 
# later would like to prompt again on invalid input

def query(question):
    print(f"{question} Y/n?")
    choice = input().lower()
    if choice == "y":
        return True
    return False

main()


