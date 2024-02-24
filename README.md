## Text Summarizer Using Flask✨ TF-IDF Text Summarization 📝


This project implements a simple text summarizer using the Flask web framework. The summarization process is based on TF-IDF (Term Frequency-Inverse Document Frequency). Users can input text through a web interface, and the application generates a summary based on the provided input.


Project Structure
•	app.py: The main file that contains the Flask application.
•	CORE/text_summarizer.py: The module with the function for text summarization.
•	templates/index.html: The HTML template for the web interface.


Dependencies


•	Flask: A micro web framework for Python.


•	NLTK: A natural language processing library.


•	scikit-learn: A machine learning library for Python.


Features 🚀


TF-IDF Calculation 🔍<br>
The core functionality of the project revolves around calculating TF-IDF scores for words in the input text. TF-IDF scores help identify the significance of each word in the context of the entire document corpus.

Sentence Extraction 📄
Using TF-IDF scores, the system extracts the most important sentences from the original text. These sentences encapsulate the essential information and contribute to the final summary.
Installation
1.	Install the required Python packages:
bashCopy code
pip install Flask nltk scikit-learn 
2.	Download NLTK data:
pythonCopy code
import nltk nltk.download('punkt') nltk.download('stopwords') 
3.	Run the Flask application:
bashCopy code
python app.py 
4.	Access the web interface at http://localhost:5000 in your browser.
Usage
1.	Enter the text you want to summarize in the provided textarea.
2.	Optionally, specify the number of sentences for the summary.
3.	Click the "Summarize" button.
4.	View the original text and the generated summary.
Notes
•	This project uses a TF-IDF-based extractive summarization approach.
•	The summarization function is located in the CORE/text_summarizer.py file.
•	Adjust the parameters in the tfidf_summarize function for desired summarization length.
Future Improvements
•	Explore more advanced summarization methods, such as BERT-based models.
•	Enhance the user interface with additional features.
