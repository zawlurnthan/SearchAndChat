from flask import Flask, render_template, request

from chat import answer_question
from search import search_topic

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    topic = ''
    data = {}
    if request.method == 'POST':
        topic = request.form['user_input']

        # Search the internet for information about the topic
        data = search_topic(topic)

    return render_template('search.html', user_input=topic, data=data)


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    question = ''
    answer = ''
    if request.method == 'POST':
        # Allow the user to ask questions about the topic
        question = request.form['question']
        # Answer the user's question using the search result as context
        answer = answer_question(question)
    return render_template('chat.html', question=question, answer=answer)


if __name__ == '__main__':
    app.run()
