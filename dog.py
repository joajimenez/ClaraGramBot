import requests

url = "https://dog.ceo/api/breeds/image/random"

def get_dog():
    try:
        res = requests.get(url)
        photo = res.json()["message"]
        return photo
    except ConnectionError:
        print(f"Error-error. Something wrong happened. {ConnectionError}")
        
# print(get_dog())