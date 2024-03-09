import urllib
import json
from abc import ABC
from abc import abstractmethod
from collections import namedtuple
from functools import reduce


url = "https://ws.audioscrobbler.com/2.0"
API_KEY_2 = "0356663ee33a0a5d27428b1f63011652"


class LastFMAPIError(Exception):
    """
    Custom Exception class to catch any potential
    exceptions in this module.
    """
    pass


lastFMTuple = namedtuple("LastFMTuple", ["data", "names_list", "play_list"])


class LastFM():
    def __init__(self, artist):
        self.api_key = None
        self.artist = artist
        self.data = None
        self.url = None
        self.baseurl = None
        self.total_songs = None
        self.total_plays = None
        self.names_list = None
        self.play_list = None

    def _download_url(self, url: str) -> dict:
        """
        Requests and returns response from API.
        """
        resp = None
        resp_obj = None
        try:
            resp = urllib.request.urlopen(url)
            json_results = resp.read()
            resp_obj = json.loads(json_results)
        except urllib.error.HTTPError as e:
            print("Failed to download contents of URL")
            print("Status code: {}".format(e.code))
        finally:
            if resp is not None:
                resp.close()
        return resp_obj
    
    def set_apikey(self, apikey: str) -> None:
        """
        inits given apikey
        """
        self.api_key = apikey

    def load_data(self) -> None:
        """
        Gets data from API and stores it in
        data attribute as namedtuple
        """
        url = f"http://ws.audioscrobbler.com/2.0/?method=artist." + \
              f"gettoptracks&artist={self.artist}" + \
              f"&api_key={self.api_key}&format=json"
        try:
            data = self._download_url(url)
            self.data = data
            lastFM_tup = self.sort_FM_data()

            self.data = lastFM_tup.data
            self.names_list = lastFM_tup.names_list
            self.play_list = lastFM_tup.play_list
        except Exception as ex:
            raise LastFMAPIError(f"LastFM data not loaded: {ex}")

    def sort_FM_data(self) -> lastFMTuple:
        """
        Takes the data and sorts it into a tuple to be parsed in load_data
        """
        response = self.get_tracks()
        data = response[0]
        names_list = response[1]
        play_list = response[2]
        fm_tuple = lastFMTuple(data, names_list, play_list)
        return fm_tuple

    def get_tracks(self) -> tuple:
        """
        Returns a tuple list of track names and their respective playcounts
        """
        data = self.data["toptracks"]["track"]
        try:
            song_entries = list(filter(lambda d:
                                       ("name" and "playcount")
                                       in d.keys(), data))
            song_names = list(map(lambda d: d["name"], song_entries))
            self.total_songs = len(song_names)
            playcounts = list(map(lambda d: int(d["playcount"]), song_entries))
            self.total_plays = reduce(lambda x, y: int(x) + int(y), playcounts)
            songs_counts = list(map(lambda x, y:
                                    (x, y),
                                    song_names,
                                    playcounts))
        except Exception as ex:
            raise LastFMAPIError(f"get_top_track unsuccesful: {ex}")
        return songs_counts, song_names, playcounts
