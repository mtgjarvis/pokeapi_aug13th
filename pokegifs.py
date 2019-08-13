import json
import requests
import os

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
name = body["name"]
id = body["id"]
type = body["types"]
type = body["types"][0]["type"]["name"]

key = os.environ.get("GIPHY_KEY")
url = (f"https://api.giphy.com/v1/gifs/search?api_key={key}&q=pikachu&rating=g")
giphy_res = requests.get(url)
body = json.loads(giphy_res.content)
gif_url = body['data'][0]['url']
print(gif_url)