import requests
from rich import print
pokemon_name = "charizard"
url="https://pokeapi.co/api/v2/pokemon/" + pokemon_name

respone = requests.get(url)
keys = [
        "order",
        # "past_types",
        "forms",
        ]
print(respone.json())

print(type(respone.json()))
raw_data = respone.json()
my_poke = {}

for i in keys:
    my_poke[i] = raw_data[i]

print(my_poke)