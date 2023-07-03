from flask import Flask, render_template, request

from chat import answer_question
from search import search_topic

app = Flask(__name__)


# Main program
def main():
    topic = input('Enter a topic: ')

    # Search the internet for information about the topic
    title, link = search_topic(topic)

    if title and link:
        print(f"Top search result: {title}")
        print(f"Link: {link}")

        # Allow the user to ask questions about the topic
        while True:
            question = input('Ask a question (or type "exit" to quit): ')

            if question.lower() == 'exit':
                break

            # Answer the user's question using the search result as context
            answer = answer_question(question, title)

            print(f"Answer: {answer}")
    else:
        print('Failed to retrieve search results')


# @app.route('/', methods=['GET', 'POST'])
# def index():
#     user_input = ''
#     processed_text = ''
#     if request.method == 'POST':
#         user_input = request.form['user_input']
#         processed_text = user_input.upper()
#     return render_template('index.html', user_input=user_input, processed_text=processed_text)

@app.route('/', methods=['GET', 'POST'])
def index():

    topic = ''
    data = {}
    processed_text = ''
    if request.method == 'POST':
        topic = request.form['user_input']

        # Search the internet for information about the topic
        data = search_topic(topic)

        processed_text = topic.upper()
    return render_template('index.html', user_input=topic, data=data, processed_text=processed_text)


if __name__ == '__main__':
    app.run()
