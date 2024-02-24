from nltk.tokenize import sent_tokenize, word_tokenize
def calculate_stats(text):
    words = word_tokenize(text)
    total_words = len(words)

    # Calculate reading time (assuming an average reading speed of 200 words per minute)
    reading_time = total_words / 200

    return total_words, reading_time