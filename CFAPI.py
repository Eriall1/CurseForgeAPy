import requests
import sys


class CFAPI(object):
    def __init__(self, api_key) -> None:
        self.api_key: str = api_key
        self.base_url: str = "https://api.curseforge.com"
        self.headers: dict[str, str] = {
            "Accept": "application/json",
            "x-api-key": self.api_key
        }

    def query_builder(self, func, *params):
        values = dict(
            zip(func.__code__.co_varnames[:func.__code__.co_argcount][1:], params))
        return "?" + "&".join([f"{k}={v}" for k, v in values.items()])

    def get_games(self, index: int = 0, pageSize: int = 50) -> dict:
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion

        url = self.base_url + "/v1/games" + self.query_builder(this, *lvars)
        response = requests.get(url, headers=self.headers)

        return response.json()

    def get_game(self, gameID: int) -> dict:
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion

        url = self.base_url + "/v1/game/" + str(gameID)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_categories(self, gameID: int, class_id: int = "", classesOnly: bool = False) -> dict:
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion

        url = self.base_url + "/v1/categories" + \
            self.query_builder(this, *lvars)
        response = requests.get(url, headers=self.headers)

        return response.json()
