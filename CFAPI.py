from datetime import datetime
import requests
import sys
import SchemaClasses as schemas

class CFAPI(object):
    def __init__(self, api_key) -> None:
        self.api_key: str = api_key
        self.base_url: str = "https://api.curseforge.com"
        self.headers: dict[str, str] = {
            'Content-Type': 'application/json',
            "Accept": "application/json",
            "x-api-key": self.api_key
        }

    def __query_builder(self, func, *params):
        assert type(func) == type(self.get_games), "func must be a function"
        values = dict(
            zip(func.__code__.co_varnames[:func.__code__.co_argcount][1:], params))
        return "?" + "&".join([f"{k}={v}" for k, v in values.items() if v is not None])

    def get_games(self, index: int|None = None, pageSize: int|None = None) -> schemas.GetGamesResponse|schemas.ApiResponseCode:
        """
        index: A zero based index of the first item to include in the response, the limit is: (index + pageSize <= 10,000).

        pageSize: The number of items to include in the response, the default/maximum value is 50.
        """
        # region init
        # region bounds checking
        if index is not None:
            if not 0 <= index <= 10000:
                return schemas.ApiResponseCode.BadRequest
        if pageSize is not None:
            if not 0 <= pageSize <= 50:
                return schemas.ApiResponseCode.BadRequest
        if index is not None and pageSize is not None:
            if not index + pageSize <= 10000:
                return schemas.ApiResponseCode.BadRequest
        # endregion
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/games{self.__query_builder(this, *lvars)}"
        # endregion
        
        response = requests.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetGamesResponse(**response.json())
        else:
            return status

    def get_game(self, gameId: int) -> schemas.GetGameResponse|schemas.ApiResponseCode:
        # region init
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/games/{gameId}"
        # endregion

        response = requests.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetGameResponse(**response.json())
        else:
            return status

    def get_versions(self, gameId: int) -> schemas.GetVersionsResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/games/{gameId}/versions"
        # endregion

        response = requests.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetVersionsResponse(**response.json())
        else:
            return status

    def get_version_types(self, gameId: int) -> schemas.GetVersionTypesResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/games/{gameId}/version-types"
        # endregion
        
        response = requests.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetVersionTypesResponse(**response.json())
        else:
            return status

    def get_categories(self, gameId: int, class_id: int|None = None, classesOnly: bool|None = None) -> schemas.GetCategoriesResponse|schemas.ApiResponseCode:
        # region init
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/games/{gameId}/version-types"
        # endregion
        
        response = requests.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetCategoriesResponse(**response.json())
        else:
            return status

    def search_mods(self, gameId: int, classId: int|None = None, categoryId: int|None = None, gameVersion: str|None = None, searchFilter: str|None = None, sortField: schemas.ModSearchSortField|None = None, sortOrder: schemas.SortOrder|None = None, modLoaderType: schemas.ModLoaderType|None = None, gameVersionTypeId: int|None = None, slug: str|None = None, index: int|None = None, pageSize: int|None = None) -> schemas.SearchModsResponse|schemas.ApiResponseCode:
        # region init
        # region bounds checking
        if index is not None:
            if not 0 <= index <= 10000:
                return schemas.ApiResponseCode.BadRequest
        if pageSize is not None:
            if not 0 <= pageSize <= 50:
                return schemas.ApiResponseCode.BadRequest
        if index is not None and pageSize is not None:
            if not index + pageSize <= 10000:
                return schemas.ApiResponseCode.BadRequest
        # endregion
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/mods/search{self.__query_builder(this, *lvars)}"
        # endregion

        response = requests.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.SearchModsResponse(**response.json())
        else:
            return status

    def get_mod(self, modId: int) -> schemas.GetModResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods/{modId}"
        # endregion

        response = requests.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetModResponse(**response.json())
        else:
            return status

    def get_mods(self, modIds: schemas.GetModsByIdsListRequestBody|list[int]) -> schemas.GetModsResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods"
        # endregion

        if isinstance(modIds, list):
            modIds = schemas.GetModsByIdsListRequestBody(modIds)
        response = requests.post(url, headers=self.headers, data=str(modIds))
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetModsResponse(**response.json())
        else:
            return status

    def get_featured_mods(self, body: schemas.GetFeaturedModsRequestBody) -> schemas.GetFeaturedModsResponse|schemas.ApiResponseCode:
        
        # region init
        # endregion
        response = requests.post(self.base_url+'/v1/mods/featured', headers=self.headers, data=str(body))
        
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetFeaturedModsResponse(**response.json())
        else:
            return status

