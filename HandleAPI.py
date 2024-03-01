import requests as rq
from pandas import json_normalize
from collections import namedtuple

API_TOKEN_1 = "WGLn6CtLttBnJ0kGPZjjnY9l4UvnwUPhFsIh1KTAk5yJ5JGJ1Mc8CzsNX819"
BASE_URL = "https://api.sportmonks.com/v3/football/" # can also add fixtures
END_URL = f"?api_token={API_TOKEN_1}"

RESP_OK = "ok"
RESP_ERROR = "error"


# available_leagues = rq.get("https://api.sportmonks.com/v3/football/leagues?api_token="+API_TOKEN_1) # this is working
# available_leagues = available_leagues.json()["data"]

response = namedtuple("response", ["type", "data"])

def extract_json(json_str: str) -> response:
    pass


def format_url(infos: list) -> str:
    """
    Formats url to pass through a get request to server
    infos = ["leagues, etc."]
    """
    url = BASE_URL
    for info in infos:
        url += info
    url += END_URL
    return url


def get_data(infos: list) -> str:
    """
    Requests and gets data from API server.
    """
    url = format_url(infos)
    try:
        print(url)
        data = rq.get(url) # json_string
        data = data.json() # response type is Response, converts to dict
        resp = response(RESP_OK, data)
    except Exception:
        resp = response(RESP_ERROR, data)
    return resp


def parse_league_data(leagues_data: list):
    """
    Parse and filter leagues_data list from server
    """
    leagues_names = list(map(lambda d: d["name"], leagues_data)) # get leauge names
    leagues_names = list(filter(lambda d: not "play-offs" in d.lower(), leagues_data)) # filter out play-offs
    return leagues_names


print(get_data(["leagues"]))








