import json
import requests
import os
from random import randint

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict

def pokemon_show(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}".format(id)
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]

    key = os.environ.get("GIPHY_KEY")
    q = "slowpoke"
    rating = "g"

    url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}&rating={}".format(key, q, rating)

    res_gif = requests.get(url)
    body = json.loads(res_gif.content)
    i = randint(0, len(body["data"]) - 1)
    gif_url = body["data"][i]["url"]



    return JsonResponse({
        "id": 25,
        "name": "pikachu",
        "types": ["electric"],
        "gif": gif_url,
    })
