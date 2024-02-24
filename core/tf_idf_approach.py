from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def tfidf_summarize(text, num_sentences=5):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize words and remove stopwords
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Join filtered words back into sentences for TF-IDF vectorization
    filtered_text = " ".join(filtered_words)

    # Calculate TF-IDF scores
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([filtered_text])

    # Get feature names (words) and their corresponding TF-IDF scores
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray().flatten()

    # Create a dictionary to map each word to its TF-IDF score
    word_tfidf_map = dict(zip(feature_names, tfidf_scores))

    # Calculate the TF-IDF score for each sentence by averaging the scores of its words
    sentence_scores = []
    for sentence in sentences:
        sentence_words = [word.lower() for word in word_tokenize(sentence) if word.isalnum()]
        sentence_tfidf_scores = [word_tfidf_map[word] for word in sentence_words if word in word_tfidf_map]
        if sentence_tfidf_scores:
            sentence_score = sum(sentence_tfidf_scores) / len(sentence_tfidf_scores)
            sentence_scores.append(sentence_score)
        else:
            sentence_scores.append(0)  # Assign score 0 if sentence has no valid words

    # Sort sentences by their TF-IDF scores and get the top N sentences
    top_sentences_idx = sorted(range(len(sentence_scores)), key=lambda i: sentence_scores[i], reverse=True)[:num_sentences]
    top_sentences = [sentences[i] for i in top_sentences_idx]

    # Construct the summary by joining the top sentences
    summary = ' '.join(top_sentences)
    return summary