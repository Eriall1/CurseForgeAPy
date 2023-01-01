from datetime import datetime
from requests.utils import quote
import sys
from . import schemaClasses as schemas
import enum
import requests_cache as rqc

class CurseForgeAPI(object):
    def __init__(self, api_key) -> None:
        self.api_key: str = api_key
        self.base_url: str = "https://api.curseforge.com"
        self.headers: dict[str, str] = {
            'Content-Type': 'application/json',
            "Accept": "application/json",
            "x-api-key": self.api_key
        }

    def __query_builder(self, func, *params):
        assert type(func) == type(self.getGames), "func must be a function"

        values = {}
        for i,v in enumerate(params):
            if v is not None:
                if isinstance(v, enum.Enum):
                    v = v.value
                values[func.__code__.co_varnames[:func.__code__.co_argcount][i+1]] = v
        return "?" + "&".join([quote(f"{k}={v}", safe="=") for k, v in values.items()])

    def getGames(self, index: int|None = None, pageSize: int|None = None) -> schemas.GetGamesResponse|schemas.ApiResponseCode:
        """
        get all games from CurseForge

        index: A zero based index of the first item to include in the response, the limit is: (index + pageSize <= 10,000).

        pageSize: The number of items to include in the response, the default/maximum value is 50.
        
        returns GetGamesResponse
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
        
        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetGamesResponse(**response.json())
        else:
            return status

    def getGame(self, gameId: int) -> schemas.GetGameResponse|schemas.ApiResponseCode:
        """
        Get a specific game from CurseForge

        gameId: The id of the game to get

        returns GetGameResponse
        """

        # region init
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/games/{gameId}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetGameResponse(**response.json())
        else:
            return status

    def getVersions(self, gameId: int) -> schemas.GetVersionsResponse|schemas.ApiResponseCode:
        """
        Get all versions for a specific game

        gameId: The id of the game to get versions for

        returns GetVersionsResponse
        """
        
        # region init
        url = self.base_url + f"/v1/games/{gameId}/versions"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetVersionsResponse(**response.json())
        else:
            return status

    def getVersionTypes(self, gameId: int) -> schemas.GetVersionTypesResponse|schemas.ApiResponseCode:
        """
        Get all version types for a specific game

        gameId: The id of the game to get version types for

        returns GetVersionTypesResponse
        """

        # region init
        url = self.base_url + f"/v1/games/{gameId}/version-types"
        # endregion
        
        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetVersionTypesResponse(**response.json())
        else:
            return status

    def getCategories(self, gameId: int, classId: int|None = None, classesOnly: bool|None = None) -> schemas.GetCategoriesResponse|schemas.ApiResponseCode:
        """
        Get all categories for a specific game

        gameId: The id of the game to get categories for
        classId: A unique class ID
        classesOnly: A flag used with gameId to return only classes

        returns GetCategoriesResponse
        """

        # region init
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/games/{gameId}/version-types"
        # endregion
        
        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetCategoriesResponse(**response.json())
        else:
            return status

    def searchMods(self, gameId: int, classId: int|None = None, categoryId: int|None = None, gameVersion: str|None = None, searchFilter: str|None = None, sortField: schemas.ModSearchSortField|None = None, sortOrder: schemas.SortOrder|None = None, modLoaderType: schemas.ModLoaderType|None = None, gameVersionTypeId: int|None = None, slug: str|None = None, index: int|None = None, pageSize: int|None = None) -> schemas.SearchModsResponse|schemas.ApiResponseCode:
        """
        searches for mods using the given parameters

        gameId: The id of the game to search mods for

        Optional:
        
        classId: A unique class ID
        categoryId: A unique category ID
        gameVersion: A game version
        searchFilter: A search filter
        sortField: A sort field
        sortOrder: A sort order
        modLoaderType: A mod loader type
        gameVersionTypeId: A game version type ID
        slug: A slug
        index: The index of the first result to return
        pageSize: The number of results to return

        returns SearchModsResponse

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
        url = self.base_url + f"/v1/mods/search{self.__query_builder(this, *lvars)}"
        # endregion
        
        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.SearchModsResponse(**response.json())
        else:
            return status

    def getMod(self, modId: int) -> schemas.GetModResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods/{modId}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetModResponse(**response.json())
        else:
            return status

    def getMods(self, modIds: schemas.GetModsByIdsListRequestBody|list[int]) -> schemas.GetModsResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods"
        # endregion

        if isinstance(modIds, list):
            modIds = schemas.GetModsByIdsListRequestBody(modIds)
        response = self.csesh.post(url, headers=self.headers, data=str(modIds))
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetModsResponse(**response.json())
        else:
            return status

    def getFeatured_mods(self, body: schemas.GetFeaturedModsRequestBody) -> schemas.GetFeaturedModsResponse|schemas.ApiResponseCode:        
        # region init
        # endregion
        response = self.csesh.post(self.base_url+'/v1/mods/featured', headers=self.headers, data=str(body))
        
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetFeaturedModsResponse(**response.json())
        else:
            return status

    def getModDescription(self, modId: int) -> schemas.StringResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods/{modId}/description"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.StringResponse(**response.json())
        else:
            return status
    
    def getModFile(self, modId: int, fileId: int) -> schemas.GetModFileResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods/{modId}/files/{fileId}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetModFileResponse(**response.json())
        else:
            return status
    
    def getModFiles(self, modId: int, gameVersion: int|None = None, modLoaderType: schemas.ModLoaderType|None = None, gameVersionTypeId: int|None = None, index: int|None = None, pageSize: int|None = None) -> schemas.GetModFilesResponse|schemas.ApiResponseCode:
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
        url = self.base_url + f"/v1/mods/{modId}/files{self.__query_builder(this, *lvars)}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetModFilesResponse(**response.json())
        else:
            return status

    def getFiles(self, body: schemas.GetModFilesRequestBody) -> schemas.GetFilesResponse|schemas.ApiResponseCode:
        # region init
        # endregion
        response = self.csesh.post(self.base_url+'/v1/mods/files', headers=self.headers, data=str(body))
        
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetFilesResponse(**response.json())
        else:
            return status

    def getModFileChangelog(self, modId: int, fileId: int) -> schemas.StringResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods/{modId}/files/{fileId}/changelog"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.StringResponse(**response.json())
        else:
            return status

    def getModFileDownloadUrl(self, modId: int, fileId: int) -> schemas.StringResponse|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/mods/{modId}/files/{fileId}/download-url"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.StringResponse(**response.json())
        else:
            return status

    def getFingerprintsMatches(self, body: schemas.GetFingerprintMatchesRequestBody) -> schemas.GetFingerprintMatchesResponse|schemas.ApiResponseCode:
        # region init
        # endregion
        response = self.csesh.post(self.base_url+'/v1/fingerprints/', headers=self.headers, data=str(body))
        
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetFingerprintMatchesResponse(**response.json())
        else:
            return status

    def getFingerprintsFuzzyMatches(self, body: schemas.GetFuzzyMatchesRequestBody) -> schemas.GetFingerprintsFuzzyMatchesResponse|schemas.ApiResponseCode:
        # region init
        # endregion
        response = self.csesh.post(self.base_url+'/v1/fingerprints/fuzzy', headers=self.headers, data=str(body))
        
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.GetFingerprintsFuzzyMatchesResponse(**response.json())
        else:
            return status

    def getMinecraftVersions(self, sortDescending: bool|None = None) -> schemas.ApiResponseOfListOfMinecraftGameVersion|schemas.ApiResponseCode:
        # region init
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/minecraft/version{self.__query_builder(this, *lvars)}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.ApiResponseOfListOfMinecraftGameVersion(**response.json())
        else:
            return status
    
    def getSpecificMinecraftVersion(self, version: str) -> schemas.ApiResponseOfMinecraftGameVersion|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/minecraft/version/{version}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.ApiResponseOfMinecraftGameVersion(**response.json())
        else:
            return status

    def getMinecraftModloaders(self, version: str|None = None, includeAll: bool|None = None) -> schemas.ApiResponseOfListOfMinecraftModLoaderIndex | schemas.ApiResponseCode:
        # region init
        # region this init
        this = eval(f"self.{sys._getframe().f_code.co_name}")
        lvars = []
        for i in this.__code__.co_varnames[:this.__code__.co_argcount][1:]:
            lvars.append(locals()[i])
        # endregion
        url = self.base_url + f"/v1/minecraft/modloader{self.__query_builder(this, *lvars)}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.ApiResponseOfListOfMinecraftModLoaderIndex(**response.json())
        else:
            return status
    
    def getSpecificMinecraftModloader(self, modLoaderName: str) -> schemas.ApiResponseOfMinecraftModLoaderVersion|schemas.ApiResponseCode:
        # region init
        url = self.base_url + f"/v1/minecraft/modloader/{modLoaderName}"
        # endregion

        response = self.csesh.get(url, headers=self.headers)
        status = schemas.ApiResponseCode(response.status_code)

        if status == schemas.ApiResponseCode.OK:
            return schemas.ApiResponseOfMinecraftModLoaderVersion(**response.json())
        else:
            return status