import requests

from constants import API_KEY


def query(search_query=''):
    if len(search_query)==0:
        return None

    req_uri = f'http://api.springernature.com/metadata/json?q=keyword:${search_query}&api_key={API_KEY}'
    res = requests.get(req_uri)
    return res.json()

# # Retrieve the author's data, fill-in, and print
# search_query = scholarly..earch_pubs('Steven A Cholewiak')
# author = scholarly.fill(next(search_query))
# print(author)

# # Print the titles of the author's publications
# print([pub['bib']['title'] for pub in author['publications']])

# # Take a closer look at the first publication
# pub = scholarly.fill(author['publications'][0])
# print(pub)

# # Which papers cited that publication?
# print([citation['bib']['title'] for citation in scholarly.citedby(pub)])