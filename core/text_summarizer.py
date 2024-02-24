# text_summarizer funtion is responsible to summarize the data 

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer




def summarize_text(text):
    sentences = sent_tokenize(text)
    print(sentences)
    words = word_tokenize(text)
    print(words)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    print(stop_words)
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Calculate word frequency
    freq = FreqDist(filtered_words)

    # Select the most frequent words as key points
    key_points = [word for word, freq in freq.most_common(5)]

    # Reconstruct the summary
    summary = [sentence for sentence in sentences if any(word in sentence for word in key_points)]
    return TreebankWordDetokenizer().detokenize(summary)
