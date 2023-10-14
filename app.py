from flask import Flask, render_template, request
from scripts import scrapper

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_input', methods=['POST'])
def process_input():
    print('debug fn running')
    user_input = request.form['user_input']

    response = scrapper.get_info(user_input)

    return response


if __name__ == '__main__':
    app.run(debug=True)
