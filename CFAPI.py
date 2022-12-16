from datetime import datetime
import requests
import sys
import SchemaClasses as sc


class CFAPI(object):
    def __init__(self, api_key) -> None:
        self.api_key: str = api_key
        self.base_url: str = "https://api.curseforge.com"
        self.headers: dict[str, str] = {
            "Accept": "application/json",
            "x-api-key": self.api_key
        }

    def query_builder(self, func, *params):
        print(type(func))
        print(func)
        assert type(func) == type(self.get_games), "func must be a function"
        values = dict(
            zip(func.__code__.co_varnames[:func.__code__.co_argcount][1:], params))
        return "?" + "&".join([f"{k}={v}" for k, v in values.items() if v is not None])

    def get_games(self, index: int|None = None, pageSize: int|None = None) -> dict|int:
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion

        url = self.base_url + "/v1/games" + self.query_builder(this, *lvars)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_game(self, gameID: int) -> dict|int:
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion

        url = self.base_url + "/v1/game/" + str(gameID)
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_versions(self, gameID: int) -> dict|int:
        url = self.base_url + "/v1/game/" + str(gameID) + "/versions"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_version_types(self, gameID: int) -> dict|int:
        url = self.base_url + "/v1/game/" + str(gameID) + "/version-types"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def get_categories(self, gameID: int, class_id: int|None = None, classesOnly: bool|None = None) -> dict|int:
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion

        url = self.base_url + "/v1/categories" + \
            self.query_builder(this, *lvars)
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    #def search_mods(self, gameID: int, classID: int, categoryID: int, gameVersion: str, searchFilter: str, sortField: )