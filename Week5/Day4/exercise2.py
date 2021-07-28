import requests

response = requests.get('https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')
if response.status_code == 200:
    if int(response.json()["data"][0]["images"]["original"]["height"]) >100:
        print(response.json()["data"][0]["images"]["original"]["width"])