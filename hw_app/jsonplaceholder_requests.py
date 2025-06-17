from typing import Any

import requests

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_json(url: str) -> Any:
    response = requests.get(url).json()
    # with requests.ClientSession() as session:
    #     with session.get(url) as response:
    return response
