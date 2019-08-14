from django.http import JsonResponse
import json
import requests
import os


def poke_search(request, query):
    
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(query)
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body['name']
    poke_id = body['id']
    types = body["types"][0]["type"]["name"]

    key = os.environ.get("GIPHY_KEY")
    url = (f"https://api.giphy.com/v1/gifs/search?api_key={key}&q=pikachu&rating=g")
    giphy_res = requests.get(url)
    body = json.loads(giphy_res.content)
    gif_url = body['data'][0]['url']

    return JsonResponse({'name': name, 'types': types, 'ID': poke_id, 'gif': gif_url})
