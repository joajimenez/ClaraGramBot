import requests

url = "https://yesno.wtf/api/"


def yes_or_no():
    try:
        res = requests.get(url)
        data = res.json()
        image = data["image"]
        assert isinstance(image, object)
        return image
    except ConnectionError:
        print(f"Error-error. Something wrong happened. {ConnectionError}")
