import os

import openai

# Set up OpenAI API credentials
openai.api_key = os.environ['OPENAI_API_KEY']


# Function to answer user questions using OpenAI GPT-3.5 model
def answer_question(question):  # context
    # Set the GPT-3.5 model parameters
    model = "text-davinci-003"
    max_tokens = 50

    # Generate an answer to the question using the GPT-3.5 model
    response = openai.Completion.create(
        engine=model,
        prompt=question,     # + '\nContext: ' + context,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # Extract the answer from the response
    return response.choices[0].text.strip()

