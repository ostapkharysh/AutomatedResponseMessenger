from flask import Flask, request
from flask_cors import CORS
from flask import render_template

app = Flask(__name__)
CORS(app)


@app.route('/')
def main_page():
    return "Hello world"


@app.route('/api/v1', methods=['POST'])
def receive_post():
    return request.form['helper']


@app.route('/main')
def main():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
