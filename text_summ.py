from flask import Flask, request, render_template
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from collections import Counter


nltk.download("punkt")
nltk.download("stopwords")

app = Flask(__name__)

def summarize_text(text, num_sentences=3):
    """
    Summarizes the input text by extracting key sentences.
    """
    if not text or len(text.split()) < num_sentences:
        return text  # Return original text if it's too short

    sentences = sent_tokenize(text)  # Split text into sentences
    words = [word.lower() for word in text.split() if word.isalnum()]
    
    stop_words = set(stopwords.words("english"))
    words = [word for word in words if word not in stop_words]
    
    word_freq = Counter(words)  # Count word frequencies
    sentence_scores = {sentence: sum(word_freq.get(word.lower(), 0) for word in sentence.split()) for sentence in sentences}

    # Select the top-ranked sentences
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    return " ".join(summarized_sentences)  # Join sentences to form summary

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        user_input = request.form["user_text"]
        summary = summarize_text(user_input, num_sentences=3)  # Adjusted for better summarization

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)



