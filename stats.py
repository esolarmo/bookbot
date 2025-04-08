def get_num_words(content):
    words = []
    words = content.split()
    word_count = 0
    for word in words:
        word_count += 1
    
    print(f"{word_count} words found in the document")
