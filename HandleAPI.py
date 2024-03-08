import requests as rq
from pandas import json_normalize
from collections import namedtuple
import urllib
from urllib import request
import json

# API_TOKEN_1 = "WGLn6CtLttBnJ0kGPZjjnY9l4UvnwUPhFsIh1KTAk5yJ5JGJ1Mc8CzsNX819"
# BASE_URL = "https://api.sportmonks.com/v3/football/" # can also add fixtures
# END_URL = f"?api_token={API_TOKEN_1}"

RESP_OK = "ok"
RESP_ERROR = "error"




# available_leagues = rq.get("https://api.sportmonks.com/v3/football/leagues?api_token="+API_TOKEN_1)
# this is working
# available_leagues = available_leagues.json()["data"]

response = namedtuple("response", ["type", "data"])


class APIHandlerException(Exception):
    """
    Custom class for exceptions in the HandleAPI module.
    """
    pass

class last_FM():
    def __init__(self):
        self.url = None
        self.data = None
        self.apikey = None

    def set_url(self, url: str) -> None:
        self.url = url

    def set_api_key(self, apikey: str) -> None:
        self.apikey = apikey

    def get_data(self, url: str) -> None:
        """
        Requests and gets data from API server.
        """
        try:
            data = rq.get(url) # json_string
            data = data.json() # response type is Response, converts to dict
            resp = self.extract_json(RESP_OK, data) # this is a tuple
        except Exception:
            print("error")
            resp = self.extract_json(RESP_ERROR, data)
        self.data = resp.data 


    def extract_json(self, type: str, json_obj: dict) -> response:
        """
        Converts a json objecti(dict) into a namedtuple to be parsed by extrenal functions.
        """
        try:
            resp = response(type, json_obj)
            return resp
        except Exception as ex:
            raise APIHandlerException("Something went wrong when extracting json", ex)
        
    def _download_url(self, url: str) -> None:
        """
        Requests and returns response from API.
        """
        resp = None
        resp_obj = None
        try:
            resp = urllib.request.urlopen(url)
            json_results = resp.read()
            resp_obj = json.loads(json_results)
            parsed_response = self.extract_json(RESP_OK, resp_obj)
            self.data = parsed_response.data
        except urllib.error.HTTPError as e:
            print("Failed to download contents of URL")
            print("Status code: {}".format(e.code))
        finally:
            if resp is not None:
                resp.close()


def get_leagues():
    """
    Parse and filter leagues_data list from server
    """
    api_obj_leagues = sportmonks_API()
    api_obj_leagues.set_api_key(API_TOKEN_1)
    url = f"https://api.sportmonks.com/v3/football/leagues?api_token={api_obj_leagues.apikey}"
    api_obj_leagues._download_url(url)
    

    leagues_data = api_obj_leagues.data["data"]
    leagues_names = list(map(lambda d: d["name"], leagues_data)) # get league names
    leagues_names = list(filter(lambda d: not "play-offs" in d.lower(), leagues_names)) # filter out play-offs
    return leagues_names
    



