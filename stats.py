def get_book_text (path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
        #print(file_contents)

def number_words (path):
    file = get_book_text(path)
    content = file.split()
    number = len(content)
    print(f"Found {number} total words")


def count_char (path):
    letters = {}
    file = get_book_text(path)
    content = file.split()
    
    for word in content:
        minus = word.lower()
        for letter in minus:
            try:
                letters[letter] += 1
            except:
                letters[letter] = 1
                
    return letters

def print_dic(dic):
    order = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    for key, value in order:
        if key.isalpha():
            print(f"{key}: {value}")