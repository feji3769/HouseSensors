import requests


def post_data(location, load):
    print(location)
    r = requests.post(location,data = load)
    print(r.text)
