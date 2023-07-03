# Function to search the internet using the Google Search API
import os

import requests


def search_topic(topic):
    # Set Google Search API key
    api_key = os.environ['GOOGLE_API_KEY']

    # Set the search engine ID
    engine_id = os.environ['SEARCH_ENGINE_ID']

    # Format the topic for search query
    query = topic.replace(' ', '+')

    # Set the Google Search API endpoint
    url = f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={engine_id}&q={query}'

    # Send a GET request to retrieve the search results
    response = requests.get(url)

    if response.status_code == 200:
        # Extract relevant information from the search results
        # Extract the title and URL of each search result

        # 1. get items list from the response json dictionary
        # 2. get dictionary from the item lists
        # 3. collect title and link from each dictionary
        # return the dictionary object

        data = {}
        for item in response.json()['items']:
            data[item['title']] = item['link']

        return data
    else:
        return None


