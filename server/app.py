from flask import Flask, request
from flask_cors import CORS
from flask import render_template
from notebooks.scripts.word_predic import markov_model

app = Flask(__name__)
CORS(app)


@app.route('/')
def main_page():
    return "Hello world"


@app.route('/api/v1', methods=['POST'])
def receive_post():
    predicted_word = ""
    first_word = request.data.decode("utf-8")
    if first_word and first_word in markov_model.second_word:
        predicted_word = markov_model.sample_word(markov_model.second_word[first_word])
    # print(first_word, predicted_word)
    return predicted_word


@app.route('/main')
def main():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
