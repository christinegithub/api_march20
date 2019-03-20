import json
import requests
import os

res = requests.get("https://pokeapi.co/api/v2/pokemon/79")
body = json.loads(res.content)

name = body["name"]
id = body["id"]
types = body["types"]

# print(name)
# print(id)
# print(types)

# pokegif_url = "https://giphy.com/gifs/pokemon-pokegraphic-gif-10j4vi4rLl4anS"

key = os.environ.get("GIPHY_KEY")
q = "slowpoke"
rating = "g"

url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}&rating={}".format(key, q, rating)

requests.get(url)

print(url)
