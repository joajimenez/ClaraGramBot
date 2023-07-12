import requests


def get_beers():
    url = "https://api.punkapi.com/v2/beers/random"
    try:
        res = requests.get(url)
        data = res.json()

        beer = {
            "name": data[0]["name"],
            "description": data[0]["description"],
            "image": data[0]["image_url"],
            "food_pairing": data[0]["food_pairing"],
        }

        return beer
    except ConnectionError:
        print(f"Error-error. Something wrong happened. {ConnectionError}")


# print(get_beers())
