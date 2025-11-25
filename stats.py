def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    dict_chars = {}
    for char in text:
        dict_chars[char.lower()] = dict_chars.get(char.lower(), 0) + 1
    return dict_chars

def dictionary_sorter(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


        