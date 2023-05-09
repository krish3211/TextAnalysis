from collections import Counter
from flask import Flask, request, render_template,jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/analysis', methods=['POST', 'GET'])
def analysis():
    if request.method == 'POST':
        text = request.form['text']
        word_count = len(text.split())
        letter_count = len(text)
        word_freq = Counter(text.split())
        most_freq_words = word_freq.most_common(5)
        least_freq_words = word_freq.most_common()[:-6:-1]
        letter_freq = Counter(text.lower())
        most_freq_letter = letter_freq.most_common()[1:6]
        least_freq_letter = letter_freq.most_common()[:-6:-1]
        # print(f"Number of words: {word_count}")
        # print(f"Number of letters: {letter_count}")
        # print(f"Most frequent words: {most_freq_words}")
        # print(f"Least frequent words: {least_freq_words}")
        # print(f"Most frequent letter: {most_freq_letter}")
        # print(f"Least frequent letter: {least_freq_letter}")
        dic = {"WordCount":word_count,
               "LetterCount":letter_count,
               "MostFWords":most_freq_words,
               "LeastFWords":least_freq_words,
               "MostFLetter":most_freq_letter,
               "LeastFLetter":least_freq_letter}
        
        return render_template("Analysis.html",preview=text,dic=dic)


if __name__ == '__main__':
    app.run()
