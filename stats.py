def get_num_words(content):
    words = []
    words = content.split()
    word_count = 0
    for word in words:
        word_count += 1
    
    # print(f"{word_count} words found in the document")
    return(word_count)

def get_num_chars(content):
    char_counts = {}

    for char in content:
        char = char.lower()
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    #print(char_counts)
    return(char_counts)

def sort_on(dict):
    return dict["num"]

def sorted_counts(char_counts):
    sorted_list = []
    
    for char in char_counts:
        dict = {}        
        dict["char"] = char
        dict["num"] = char_counts[char]
        sorted_list.append(dict)
        

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list
    

    




