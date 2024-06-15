def count_words(text):
    words = text.split()
    return len(words)

def unique_words(text):
    words = text.lower().split()
    return set(words)