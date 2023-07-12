import requests

url = "http://thecatapi.com/api/images/get"


def get_cat():
    try:
        res = requests.get(url)
        photo = res.url
        return photo
    except ConnectionError:
        print(f"Error-error. Something wrong happened. {ConnectionError}")


# print(get_cat())
