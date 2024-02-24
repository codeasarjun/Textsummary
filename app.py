from flask import Flask, render_template, request
import nltk
from core.text_summarizer import summarize_text
from core.calualte_time import calculate_stats
from core.tf_idf_approach import tfidf_summarize

nltk.download('punkt')


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        text = request.form['text']

        # Calculate stats for original text
        original_total_words, original_reading_time = calculate_stats(text)

        summary = tfidf_summarize(text)
        # Calculate stats for the summary
        summary_total_words, summary_reading_time = calculate_stats(summary)

        return render_template('index.html', 
                               original_text=text,
                               summary=summary,
                               original_total_words=original_total_words,
                               original_reading_time=original_reading_time,
                               summary_total_words=summary_total_words,
                               summary_reading_time=summary_reading_time)

if __name__ == '__main__':
    app.run(debug=True)
