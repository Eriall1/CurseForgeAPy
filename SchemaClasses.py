from __future__ import annotations
import enum
from datetime import datetime


#region Schemas
# ApiResponseOfListOfMinecraftGameVersion Schema
"""
Properties
Name 	Type 	Description
data 	[MinecraftGameVersion] 	The response data
"""

# ApiResponseOfListOfMinecraftGameVersion Class
class ApiResponseOfListOfMinecraftGameVersion(object):
    def __init__(self, data: list[MinecraftGameVersion]):
        self.data: list[MinecraftGameVersion] = list(map(lambda x: MinecraftGameVersion(**x) if isinstance(x, dict) else x, data))

# ApiResponseOfListOfMinecraftModLoaderIndex Schema
"""
Properties
Name 	Type 	Description
data 	[MinecraftModLoaderIndex] 	The response data
"""

# ApiResponseOfListOfMinecraftModLoaderIndex Class
class ApiResponseOfListOfMinecraftModLoaderIndex(object):
    def __init__(self, data: list[MinecraftModLoaderIndex]):
        self.data: list[MinecraftModLoaderIndex] = list(map(lambda x: MinecraftModLoaderIndex(**x) if isinstance(x, dict) else x, data))

# ApiResponseOfMinecraftGameVersion Schema
"""
Properties
Name 	Type 	Description
data 	MinecraftGameVersion 	The response data
"""

# ApiResponseOfMinecraftGameVersion Class
class ApiResponseOfMinecraftGameVersion(object):
    def __init__(self, data: MinecraftGameVersion):
        self.data: MinecraftGameVersion = MinecraftGameVersion(**data) if isinstance(data, dict) else data

# ApiResponseOfMinecraftModLoaderVersion Schema
"""
Properties
Name 	Type 	Description
data 	MinecraftModLoaderVersion 	The response data
"""

# ApiResponseOfMinecraftModLoaderVersion Class
class ApiResponseOfMinecraftModLoaderVersion(object):
    def __init__(self, data: MinecraftModLoaderVersion):
        self.data: MinecraftModLoaderVersion = MinecraftModLoaderVersion(**data) if isinstance(data, dict) else data

# Category Schema
"""Properties
Name 	Type 	Description
id 	integer(int32) 	The category id
gameId 	integer(int32) 	The game id related to the category
name 	string 	Category name
slug 	string 	The category slug as it appear in the URL
url 	string 	The category URL
iconUrl 	string 	URL for the category icon
dateModified 	string(date-time) 	Last modified date of the category
isClass 	boolean¦null 	A top level category for other categories
classId 	integer(int32)¦null 	The class id of the category, meaning - the class of which this category is under
parentCategoryId 	integer(int32)¦null 	The parent category for this category
displayIndex 	integer(int32)¦null 	The display index for this category
"""

# Category Class
class Category(object):  
    def __init__(self, id, gameId: int, name: str, slug: str, url: str, iconUrl: str, dateModified: datetime, isClass: bool|None = None, classId: int|None = None, parentCategoryId: int|None = None, displayIndex: int|None = None):
        self.id: int = int(id)
        self.gameId: int = int(gameId)
        self.name: str = str(name)
        self.slug: str = str(slug)
        self.url: str = str(url)
        self.iconUrl: str = iconUrl
        self.dateModified: datetime = datetime.strptime(dateModified, "%Y-%m-%dT%H:%M:%S.%fZ") if isinstance(dateModified, str) else dateModified
        self.isClass: bool | None = bool(isClass) if isClass is not None else None
        self.classId: int | None = int(classId) if classId is not None else None
        self.parentCategoryId: int | None = int(parentCategoryId) if parentCategoryId is not None else None
        self.displayIndex: int | None = int(displayIndex) if displayIndex is not None else None

# CoreApiStatus Schema
"""
CoreApiStatus

Possible enum values:

1=Private

2=Public
"""

# CoreApiStatus Enum
class CoreApiStatus(enum.Enum):
    Private = 1
    Public = 2


# CoreStatus Schema
"""
CoreStatus

Possible enum values:

1=Draft

2=Test

3=PendingReview

4=Rejected

5=Approved

6=Live
"""

# CoreStatus Enum
class CoreStatus(enum.Enum):
    Draft = 1
    Test = 2
    PendingReview = 3
    Rejected = 4
    Approved = 5
    Live = 6

# FeaturedModsResponse Schema
"""
Properties
Name 	Type 	Description
featured 	[Mod] 	none
popular 	[Mod] 	none
recentlyUpdated 	[Mod] 	none
"""

# FeaturedModsResponse Class
class FeaturedModsResponse(object):
    def __init__(self, featured: list[Mod], popular: list[Mod], recentlyUpdated: list[Mod]):
        self.featured: list[Mod] = list(map(lambda x: Mod(**x) if isinstance(x, dict) else x, featured))
        self.popular: list[Mod] = list(map(lambda x: Mod(**x) if isinstance(x, dict) else x, popular))
        self.recentlyUpdated: list[Mod] = list(map(lambda x: Mod(**x) if isinstance(x, dict) else x, recentlyUpdated))

# File Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	The file id
gameId 	integer(int32) 	The game id related to the mod that this file belongs to
modId 	integer(int32) 	The mod id
isAvailable 	boolean 	Whether the file is available to download
displayName 	string 	Display name of the file
fileName 	string 	Exact file name
releaseType 	FileReleaseType 	The file release type
fileStatus 	FileStatus 	Status of the file
hashes 	[FileHash] 	The file hash (i.e. md5 or sha1)
fileDate 	string(date-time) 	The file timestamp
fileLength 	integer(int64) 	The file length in bytes
downloadCount 	integer(int64) 	The number of downloads for the file
downloadUrl 	string 	The file download URL
gameVersions 	[string] 	List of game versions this file is relevant for
sortableGameVersions 	[SortableGameVersion] 	Metadata used for sorting by game versions
dependencies 	[FileDependency] 	List of dependencies files
exposeAsAlternative 	boolean¦null 	none
parentProjectFileId 	integer(int32)¦null 	none
alternateFileId 	integer(int32)¦null 	none
isServerPack 	boolean¦null 	none
serverPackFileId 	integer(int32)¦null 	none
fileFingerprint 	integer(int64) 	none
modules 	[FileModule] 	none
"""

# File Class
class File(object):
    def __init__(self, id: int, gameId: int, modId: int, isAvailable: bool, displayName: str, fileName: str, releaseType: FileReleaseType, fileStatus: FileStatus, hashes: list[FileHash], fileDate: str, fileLength: int, downloadCount: int, downloadUrl: str, gameVersions: list[str], sortableGameVersions: list[SortableGameVersion], dependencies: list[FileDependency], fileFingerprint: int, modules: list[FileModule], exposeAsAlternative: bool | None = None, parentProjectFileId: int | None = None, alternateFileId: int | None = None, isServerPack: bool | None = None, serverPackFileId: int | None = None):
        self.id: int = int(id)
        self.gameId: int = int(gameId)
        self.modId: int = int(modId)
        self.isAvailable: bool = bool(isAvailable)
        self.displayName: str = str(displayName)
        self.fileName: str = str(fileName)
        self.releaseType: FileReleaseType = FileReleaseType(releaseType)
        self.fileStatus: FileStatus = FileStatus(fileStatus)
        self.hashes: list[FileHash] = list(map(lambda x: FileHash(**x) if isinstance(x, dict) else x, hashes))
        self.fileDate: str = str(fileDate)
        self.fileLength: int = int(fileLength)
        self.downloadCount: int = int(downloadCount)
        self.downloadUrl: str = str(downloadUrl)
        self.gameVersions: list[str] = list(map(lambda x: str(x), gameVersions))
        self.sortableGameVersions: list[SortableGameVersion] = list(map(lambda x: SortableGameVersion(**x) if isinstance(x, dict) else x, sortableGameVersions))
        self.dependencies: list[FileDependency] = list(map(lambda x: FileDependency(x), dependencies))
        self.exposeAsAlternative: bool | None = bool(exposeAsAlternative) if exposeAsAlternative is not None else None
        self.parentProjectFileId: int | None = int(parentProjectFileId) if parentProjectFileId is not None else None
        self.alternateFileId: int | None = int(alternateFileId) if alternateFileId is not None else None
        self.isServerPack: bool | None = bool(isServerPack) if isServerPack is not None else None
        self.serverPackFileId: int | None = int(serverPackFileId) if serverPackFileId is not None else None
        self.fileFingerprint: int = int(fileFingerprint)
        self.modules: list[FileModule] = list(map(lambda x: FileModule(**x) if isinstance(x, dict) else x, modules))

# FileDependency Schema
"""
Properties
Name 	Type 	Description
modId 	integer(int32) 	none
relationType 	FileRelationType 	1 = EmbeddedLibrary
2 = OptionalDependency
3 = RequiredDependency
4 = Tool
5 = Incompatible
6 = Include
"""

# FileDependency Enum
class FileDependency(enum.Enum):
    EmbeddedLibrary = 1
    OptionalDependency = 2
    RequiredDependency = 3
    Tool = 4
    Incompatible = 5
    Include = 6

# FileHash Schema
"""
Properties
Name 	Type 	Description
value 	string 	none
algo 	HashAlgo 	1 = Sha1
2 = Md5
"""

# FileHash Class
class FileHash(object):
    def __init__(self, value: str, algo: HashAlgo):
        self.value: str = str(value)
        self.algo: HashAlgo = HashAlgo(algo)

# FileIndex Schema
"""
Properties
Name 	Type 	Description
gameVersion 	string 	none
fileId 	integer(int32) 	none
filename 	string 	none
releaseType 	FileReleaseType 	1 = Release
2 = Beta
3 = Alpha
gameVersionTypeId 	integer(int32)¦null 	none
modLoader 	ModLoaderType 	0 = Any
1 = Forge
2 = Cauldron
3 = LiteLoader
4 = Fabric
5 = Quilt
"""

# FileIndex Class
class FileIndex(object):
    def __init__(self, gameVersion: str, fileId: int, filename: str, releaseType: FileReleaseType, modLoader: ModLoaderType, gameVersionTypeId: int | None = None):
        self.gameVersion: str = str(gameVersion)
        self.fileId: int = int(fileId)
        self.filename: str = str(filename)
        self.releaseType: FileReleaseType = FileReleaseType(releaseType)
        self.gameVersionTypeId: int | None = int(gameVersionTypeId) if gameVersionTypeId is not None else None
        self.modLoader: ModLoaderType = ModLoaderType(modLoader)

# FileModule Schema
"""
Properties
Name 	Type 	Description
name 	string 	none
fingerprint 	integer(int64) 	none
"""

# FileModule Class
class FileModule(object):
    def __init__(self, name: str, fingerprint: int):
        self.name: str = str(name)
        self.fingerprint: int = int(fingerprint)

# FileRelationType Schema
"""
Possible enum values:

1=EmbeddedLibrary

2=OptionalDependency

3=RequiredDependency

4=Tool

5=Incompatible

6=Include
"""

# FileRelationType Class
class FileRelationType(enum.Enum):
    EmbeddedLibrary = 1
    OptionalDependency = 2
    RequiredDependency = 3
    Tool = 4
    Incompatible = 5
    Include = 6


# FileReleaseType Schema
"""
Possible enum values:

1=Release

2=Beta

3=Alpha
"""

# FileReleaseType Enum
class FileReleaseType(enum.Enum):
    Release = 1
    Beta = 2
    Alpha = 3

# FileStatus Schema
"""
Possible enum values:

1=Processing

2=ChangesRequired

3=UnderReview

4=Approved

5=Rejected

6=MalwareDetected

7=Deleted

8=Archived

9=Testing

10=Released

11=ReadyForReview

12=Deprecated

13=Baking

14=AwaitingPublishing

15=FailedPublishing
"""

# FileStatus Enum
class FileStatus(enum.Enum):
    Processing = 1
    ChangesRequired = 2
    UnderReview = 3
    Approved = 4
    Rejected = 5
    MalwareDetected = 6
    Deleted = 7
    Archived = 8
    Testing = 9
    Released = 10
    ReadyForReview = 11
    Deprecated = 12
    Baking = 13
    AwaitingPublishing = 14
    FailedPublishing = 15

# FingerprintFuzzyMatch Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
file 	File 	none
latestFiles 	[File] 	none
fingerprints 	[integer] 	none
"""

# FingerprintFuzzyMatch Class
class FingerprintFuzzyMatch(object):
    def __init__(self, id: int, file: File, latestFiles: list[File], fingerprints: list[int]):
        self.id: int = int(id)
        self.file: File = File(**file) if isinstance(file, dict) else file
        self.latestFiles: list[File] = list(map(lambda x: File(**x) if isinstance(x, dict) else x, latestFiles))
        self.fingerprints: list[int] = list(map(lambda x: int(x), fingerprints))

# FingerprintFuzzyMatchResult Schema
"""
Properties
Name 	Type 	Description
fuzzyMatches 	[FingerprintFuzzyMatch] 	none
"""

# FingerprintFuzzyMatchResult Class
class FingerprintFuzzyMatchResult(object):
    def __init__(self, fuzzyMatches: list[FingerprintFuzzyMatch]):
        self.fuzzyMatches: list[FingerprintFuzzyMatch] = list(map(lambda x: FingerprintFuzzyMatch(**x) if isinstance(x, dict) else x, fuzzyMatches))

# FingerprintMatch Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
file 	File 	none
latestFiles 	[File] 	none
"""

# FingerprintMatch Class
class FingerprintMatch(object):
    def __init__(self, id: int, file: File, latestFiles: list[File]):
        self.id: int = int(id)
        self.file: File = File(**file) if isinstance(file, dict) else file
        self.latestFiles: list[File] = list(map(lambda x: File(**x) if isinstance(x, dict) else x, latestFiles))

# FingerprintsMatchesResult Schema
"""
Properties
Name 	Type 	Description
isCacheBuilt 	boolean 	none
exactMatches 	[FingerprintMatch] 	none
exactFingerprints 	[integer] 	none
partialMatches 	[FingerprintMatch] 	none
partialMatchFingerprints 	object 	none
» additionalProperties 	[integer] 	none
installedFingerprints 	[integer] 	none
unmatchedFingerprints 	[integer] 	none
"""

# FingerprintsMatchesResult Class
class FingerprintsMatchesResult(object):
    def __init__(self, isCacheBuilt: bool, exactMatches: list[FingerprintMatch], exactFingerprints: list[int], partialMatches: list[FingerprintMatch], partialMatchFingerprints: object, installedFingerprints: list[int], unmatchedFingerprints: list[int]):
        self.isCacheBuilt: bool = bool(isCacheBuilt)
        self.exactMatches: list[FingerprintMatch] = list(map(lambda x: FingerprintMatch(**x) if isinstance(x, dict) else x, exactMatches))
        self.exactFingerprints: list[int] = list(map(int, exactFingerprints))
        self.partialMatches: list[FingerprintMatch] = partialMatches
        self.partialMatchFingerprints: object = partialMatchFingerprints
        self.installedFingerprints: list[int] = list(map(int, installedFingerprints))
        self.unmatchedFingerprints: list[int] = list(map(int, unmatchedFingerprints))

# FolderFingerprint Schema
"""
Properties
Name 	Type 	Description
foldername 	string 	none
fingerprints 	[integer] 	none
"""

# FolderFingerprint Class
class FolderFingerprint(object):
    def __init__(self, foldername: str, fingerprints: list[int]):
        self.foldername: str = str(foldername)
        self.fingerprints: list[int] = list(map(int, fingerprints))

# Game Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
name 	string 	none
slug 	string 	none
dateModified 	string(date-time) 	none
assets 	GameAssets 	none
status 	CoreStatus 	1 = Draft
2 = Test
3 = PendingReview
4 = Rejected
5 = Approved
6 = Live
apiStatus 	CoreApiStatus 	1 = Private
2 = Public
"""

# Game Class
class Game(object):
    def __init__(self, id: int, name: str, slug: str, dateModified: datetime, assets: GameAssets, status: CoreStatus, apiStatus: CoreApiStatus):
        self.id: int = int(id)
        self.name: str = str(name)
        self.slug: str = str(slug)
        self.dateModified: datetime = datetime.strptime(dateModified, "%Y-%m-%dT%XZ") if isinstance(dateModified, str) else dateModified
        self.assets: GameAssets = GameAssets(**assets) if isinstance(assets, dict) else assets
        self.status: CoreStatus = CoreStatus(status)
        self.apiStatus: CoreApiStatus = CoreApiStatus(apiStatus)

# GameAssets Schema
"""
Properties
Name 	Type 	Description
iconUrl 	string 	none
tileUrl 	string 	none
coverUrl 	string 	none
"""

# GameAssets Class
class GameAssets(object):
    def __init__(self, iconUrl: str, tileUrl: str, coverUrl: str):
        self.iconUrl: str = str(iconUrl)
        self.tileUrl: str = str(tileUrl)
        self.coverUrl: str = str(coverUrl)

# GameVersionsByType Schema
"""
Properties
Name 	Type 	Description
type 	integer(int32) 	none
versions 	[string] 	none
"""

# GameVersionsByType Class
class GameVersionsByType(object):
    def __init__(self, type: int, versions: list[str]):
        self.type: int = int(type)
        self.versions: list[str] = list(map(str, versions))

# GameVersionStatus Schema
"""
Possible enum values:

1=Approved

2=Deleted

3=New
"""

# GameVersionStatus Enum
class GameVersionStatus(enum.Enum):
    Approved = 1
    Deleted = 2
    New = 3

# GameVersionType Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
gameId 	integer(int32) 	none
name 	string 	none
slug 	string 	none
"""

# GameVersionType Class
class GameVersionType(object):
    def __init__(self, id: int, gameId: int, name: str, slug: str):
        self.id: int = int(id)
        self.gameId: int = int(gameId)
        self.name: str = str(name)
        self.slug: str = str(slug)

# GameVersionTypeStatus Schema
"""
Possible enum values:

1=Normal

2=Deleted
"""

# GameVersionTypeStatus Enum
class GameVersionTypeStatus(enum.Enum):
    Normal = 1
    Deleted = 2

# GetCategoriesResponse Schema
"""
Properties
Name 	Type 	Description
data 	[Category] 	The response data
"""

# GetCategoriesResponse Class
class GetCategoriesResponse(object):
    def __init__(self, data: Category):
        self.data: Category = Category(**data) if isinstance(data, dict) else data

# GetFeaturedModsResponse Schema
"""
Properties
Name 	Type 	Description
data 	FeaturedModsResponse 	The response data
"""

# GetFeaturedModsResponse Class
class GetFeaturedModsResponse(object):
    def __init__(self, data: FeaturedModsResponse):
        self.data: FeaturedModsResponse = FeaturedModsResponse(**data) if isinstance(data, dict) else data

# GetFilesResponse Schema
"""
Properties
Name 	Type 	Description
data 	[File] 	The response data
"""

# GetFilesResponse Class
class GetFilesResponse(object):
    def __init__(self, data: list[File]):
        self.data: list[File] = list(map(lambda x: File(**x) if isinstance(x, dict) else x, data))

# GetFingerprintMatchesResponse Schema
"""
Properties
Name 	Type 	Description
data 	FingerprintsMatchesResult 	The response data
"""

# GetFingerprintMatchesResponse Class
class GetFingerprintMatchesResponse(object):
    def __init__(self, data: FingerprintsMatchesResult):
        self.data: FingerprintsMatchesResult = FingerprintsMatchesResult(**data) if isinstance(data, dict) else data

# GetFingerprintsFuzzyMatchesResponse Schema
"""
Properties
Name 	Type 	Description
data 	FingerprintFuzzyMatchResult 	The response data
"""

# GetFingerprintsFuzzyMatchesResponse Class
class GetFingerprintsFuzzyMatchesResponse(object):
    def __init__(self, data: FingerprintFuzzyMatchResult):
        self.data: FingerprintFuzzyMatchResult = FingerprintFuzzyMatchResult(**data) if isinstance(data, dict) else data

# GetGameResponse Schema
"""
Properties
Name 	Type 	Description
data 	Game 	The response data
"""

# GetGameResponse Class
class GetGameResponse(object):
    def __init__(self, data: Game):
        self.data: Game = Game(**data) if isinstance(data, dict) else data

# GetGamesResponse Schema
"""
Properties
Name 	Type 	Description
data 	[Game] 	The response data
pagination 	Pagination 	The response pagination information
"""

# GetGamesResponse Class
class GetGamesResponse(object):
    def __init__(self, data: list[Game], pagination: Pagination):
        self.data: list[Game] = list(map(lambda x: Game(**x) if isinstance(x, dict) else x, data))
        self.pagination: Pagination = Pagination(**pagination) if isinstance(pagination, dict) else pagination

# GetModFileResponse Schema
"""
Properties
Name 	Type 	Description
data 	File 	The response data
"""

# GetModFileResponse Class
class GetModFileResponse(object):
    def __init__(self, data: File):
        self.data: File = File(**data) if isinstance(data, dict) else data

# GetModFilesResponse Schema
"""
Properties
Name 	Type 	Description
data 	[File] 	The response data
pagination 	Pagination 	The response pagination information
"""

# GetModFilesResponse Class
class GetModFilesResponse(object):
    def __init__(self, data: list[File], pagination: Pagination):
        self.data: list[File] = list(map(lambda x: File(**x) if isinstance(x, dict) else x, data))
        self.pagination: Pagination = Pagination(**pagination) if isinstance(pagination, dict) else pagination

# GetModResponse Schema
"""
Properties
Name 	Type 	Description
data 	Mod 	The response data
"""

# GetModResponse Class
class GetModResponse(object):
    def __init__(self, data: Mod):
        self.data: Mod = Mod(**data) if isinstance(data, dict) else data

# GetModsResponse Schema
"""
Properties
Name 	Type 	Description
data 	[Mod] 	The response data
"""

# GetModsResponse Class
class GetModsResponse(object):
    def __init__(self, data: list[Mod]):
        self.data: list[Mod] = list(map(lambda x: Mod(**x) if isinstance(x, dict) else x, data))

# GetVersionTypesResponse Schema
"""
Properties
Name 	Type 	Description
data 	[GameVersionType] 	The response data
"""

# GetVersionTypesResponse Class
class GetVersionTypesResponse(object):
    def __init__(self, data: list[GameVersionType]):
        self.data: list[GameVersionType] = list(map(lambda x: GameVersionType(**x) if isinstance(x, dict) else x, data))

# GetVersionsResponse Schema
"""
Properties
Name 	Type 	Description
data 	[GameVersionsByType] 	The response data
"""

# GetVersionsResponse Class
class GetVersionsResponse(object):
    def __init__(self, data: list[GameVersionsByType]):
        self.data: list[GameVersionsByType] = list(map(lambda x: GameVersionsByType(**x) if isinstance(x, dict) else x, data))

# GetFeaturedModsRequestBody Schema
"""
Properties
Name 	Type 	Description
gameId 	integer(int32) 	none
excludedModIds 	[integer] 	none
gameVersionTypeId 	integer(int32)¦null 	none
"""

# GetFeaturedModsRequestBody Class
class GetFeaturedModsRequestBody(object):
    def __init__(self, gameId: int, excludedModIds: list[int], gameVersionTypeId: int):
        self.gameId: int = int(gameId)
        self.excludedModIds: list[int] = list(map(int, excludedModIds))
        self.gameVersionTypeId: int = int(gameVersionTypeId)

# GetFingerprintMatchesRequestBody Schema
"""
Properties
Name 	Type 	Description
fingerprints 	[integer] 	none
"""

# GetFingerprintMatchesRequestBody Class
class GetFingerprintMatchesRequestBody(object):
    def __init__(self, fingerprints: list[int]):
        self.fingerprints: list[int] = list(map(int, fingerprints))

# GetFuzzyMatchesRequestBody Schema
"""
Properties
Name 	Type 	Description
gameId 	integer(int32) 	none
fingerprints 	[FolderFingerprint] 	none
"""

# GetFuzzyMatchesRequestBody Class
class GetFuzzyMatchesRequestBody(object):
    def __init__(self, gameId: int, fingerprints: list[FolderFingerprint]):
        self.gameId: int = int(gameId)
        self.fingerprints: list[FolderFingerprint] = list(map(lambda x: FolderFingerprint(**x) if isinstance(x, dict) else x, fingerprints))

# GetModFilesRequestBody Schema
"""
Properties
Name 	Type 	Description
fileIds 	[integer] 	none
"""

# GetModFilesRequestBody Class
class GetModFilesRequestBody(object):
    def __init__(self, fileIds: list[int]):
        self.fileIds: list[int] = list(map(int, fileIds))

# GetModsByIdsListRequestBody Schema
"""
Properties
Name 	Type 	Description
modIds 	[integer] 	none
"""

# GetModsByIdsListRequestBody Class
class GetModsByIdsListRequestBody(object):
    def __init__(self, modIds: list[int]):
        self.modIds: list[int] = list(map(int, modIds))

# HashAlgo Schema
"""
Possible enum values:

1=Sha1

2=Md5
"""

# HashAlgo Enum
class HashAlgo(enum.Enum):
    Sha1 = 1
    Md5 = 2

# MinecraftGameVersion Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
gameVersionId 	integer(int32) 	none
versionString 	string 	none
jarDownloadUrl 	string 	none
jsonDownloadUrl 	string 	none
approved 	boolean 	none
dateModified 	string(date-time) 	none
gameVersionTypeId 	integer(int32) 	none
gameVersionStatus 	GameVersionStatus 	1 = Approved
2 = Deleted
3 = New
gameVersionTypeStatus 	GameVersionTypeStatus 	1 = Normal
2 = Deleted
"""

# MinecraftGameVersion Class
class MinecraftGameVersion(object):
    def __init__(self, id: int, gameVersionId: int, versionString: str, jarDownloadUrl: str, jsonDownloadUrl: str, approved: bool, dateModified: datetime, gameVersionTypeId: int, gameVersionStatus: GameVersionStatus, gameVersionTypeStatus: GameVersionTypeStatus):
        self.id: int = int(id)
        self.gameVersionId: int = int(gameVersionId)
        self.versionString: str = str(versionString)
        self.jarDownloadUrl: str = str(jarDownloadUrl)
        self.jsonDownloadUrl: str = str(jsonDownloadUrl)
        self.approved: bool = bool(approved)
        self.dateModified: datetime = datetime.strptime(dateModified, "%Y-%m-%dT%XZ") if isinstance(dateModified, str) else dateModified
        self.gameVersionTypeId: int = int(gameVersionTypeId)
        self.gameVersionStatus: GameVersionStatus = GameVersionStatus(gameVersionStatus) 
        self.gameVersionTypeStatus: GameVersionTypeStatus = GameVersionTypeStatus(gameVersionTypeStatus)

# MinecraftModLoaderIndex Schema
"""
Properties
Name 	Type 	Description
name 	string 	none
gameVersion 	string 	none
latest 	boolean 	none
recommended 	boolean 	none
dateModified 	string(date-time) 	none
type 	ModLoaderType 	0 = Any
1 = Forge
2 = Cauldron
3 = LiteLoader
4 = Fabric
5 = Quilt
"""

# MinecraftModLoaderIndex Class
class MinecraftModLoaderIndex(object):
    def __init__(self, name: str, gameVersion: str, latest: bool, recommended: bool, dateModified: datetime, type: ModLoaderType):
        self.name: str = str(name)
        self.gameVersion: str = str(gameVersion)
        self.latest: bool = bool(latest)
        self.recommended: bool = bool(recommended)
        self.dateModified: datetime =  datetime.strptime(dateModified, "%Y-%m-%dT%XZ") if isinstance(dateModified, str) else dateModified
        self.type: ModLoaderType = ModLoaderType(type)

# MinecraftModLoaderVersion Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
gameVersionId 	integer(int32) 	none
minecraftGameVersionId 	integer(int32) 	none
forgeVersion 	string 	none
name 	string 	none
type 	ModLoaderType 	0 = Any
1 = Forge
2 = Cauldron
3 = LiteLoader
4 = Fabric
5 = Quilt
downloadUrl 	string 	none
filename 	string 	none
installMethod 	ModLoaderInstallMethod 	1 = ForgeInstaller
2 = ForgeJarInstall
3 = ForgeInstaller_v2
latest 	boolean 	none
recommended 	boolean 	none
approved 	boolean 	none
dateModified 	string(date-time) 	none
mavenVersionString 	string 	none
versionJson 	string 	none
librariesInstallLocation 	string 	none
minecraftVersion 	string 	none
additionalFilesJson 	string 	none
modLoaderGameVersionId 	integer(int32) 	none
modLoaderGameVersionTypeId 	integer(int32) 	none
modLoaderGameVersionStatus 	GameVersionStatus 	1 = Approved
2 = Deleted
3 = New
modLoaderGameVersionTypeStatus 	GameVersionTypeStatus 	1 = Normal
2 = Deleted
mcGameVersionId 	integer(int32) 	none
mcGameVersionTypeId 	integer(int32) 	none
mcGameVersionStatus 	GameVersionStatus 	1 = Approved
2 = Deleted
3 = New
mcGameVersionTypeStatus 	GameVersionTypeStatus 	1 = Normal
2 = Deleted
installProfileJson 	string 	none
"""

# MinecraftModLoaderVersion Class
class MinecraftModLoaderVersion(object):
    def __init__(self, id: int, gameVersionId: int, minecraftGameVersionId: int, forgeVersion: str, name: str, type: ModLoaderType, downloadUrl: str, filename: str, installMethod: ModLoaderInstallMethod, latest: bool, recommended: bool, approved: bool, dateModified: datetime, mavenVersionString: str, versionJson: str, librariesInstallLocation: str, minecraftVersion: str, additionalFilesJson: str, modLoaderGameVersionId: int, modLoaderGameVersionTypeId: int, modLoaderGameVersionStatus: GameVersionStatus, modLoaderGameVersionTypeStatus: GameVersionTypeStatus, mcGameVersionId: int, mcGameVersionTypeId: int, mcGameVersionStatus: GameVersionStatus, mcGameVersionTypeStatus: GameVersionTypeStatus, installProfileJson: str):
        self.id: int = int(id)
        self.gameVersionId: int = int(gameVersionId)
        self.minecraftGameVersionId: int = int(minecraftGameVersionId)
        self.forgeVersion: str = str(forgeVersion)
        self.name: str = str(name)
        self.type: ModLoaderType = ModLoaderType(type)
        self.downloadUrl: str = str(downloadUrl)
        self.filename: str = str(filename)
        self.installMethod: ModLoaderInstallMethod = ModLoaderInstallMethod(installMethod)
        self.latest: bool = bool(latest)
        self.recommended: bool = bool(recommended)
        self.approved: bool = bool(approved)
        self.dateModified: datetime = datetime.strptime(dateModified, "%Y-%m-%dT%XZ") if isinstance(dateModified, str) else dateModified
        self.mavenVersionString: str = str(mavenVersionString)
        self.versionJson: str = str(versionJson)
        self.librariesInstallLocation: str = str(librariesInstallLocation)
        self.minecraftVersion: str = str(minecraftVersion)
        self.additionalFilesJson: str = str(additionalFilesJson)
        self.modLoaderGameVersionId: int = int(modLoaderGameVersionId)
        self.modLoaderGameVersionTypeId: int = int(modLoaderGameVersionTypeId)
        self.modLoaderGameVersionStatus: GameVersionStatus = (modLoaderGameVersionStatus)
        self.modLoaderGameVersionTypeStatus: GameVersionTypeStatus = GameVersionTypeStatus(modLoaderGameVersionTypeStatus)
        self.mcGameVersionId: int = int(mcGameVersionId)
        self.mcGameVersionTypeId: int = int(mcGameVersionTypeId)
        self.mcGameVersionStatus: GameVersionStatus = GameVersionStatus(mcGameVersionStatus)
        self.mcGameVersionTypeStatus: GameVersionTypeStatus = GameVersionTypeStatus(mcGameVersionTypeStatus)
        self.installProfileJson: str = str(installProfileJson)

# Mod Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	The mod id
gameId 	integer(int32) 	The game id this mod is for
name 	string 	The name of the mod
slug 	string 	The mod slug that would appear in the URL
links 	ModLinks 	Relevant links for the mod such as Issue tracker and Wiki
summary 	string 	Mod summary
status 	ModStatus 	Current mod status
downloadCount 	integer(int64) 	Number of downloads for the mod
isFeatured 	boolean 	Whether the mod is included in the featured mods list
primaryCategoryId 	integer(int32) 	The main category of the mod as it was chosen by the mod author
categories 	[Category] 	List of categories that this mod is related to
classId 	integer(int32)¦null 	The class id this mod belongs to
authors 	[ModAuthor] 	List of the mod's authors
logo 	ModAsset 	The mod's logo asset
screenshots 	[ModAsset] 	List of screenshots assets
mainFileId 	integer(int32) 	The id of the main file of the mod
latestFiles 	[File] 	List of latest files of the mod
latestFilesIndexes 	[FileIndex] 	List of file related details for the latest files of the mod
dateCreated 	string(date-time) 	The creation date of the mod
dateModified 	string(date-time) 	The last time the mod was modified
dateReleased 	string(date-time) 	The release date of the mod
allowModDistribution 	boolean¦null 	Is mod allowed to be distributed
gamePopularityRank 	integer(int32) 	The mod popularity rank for the game
isAvailable 	boolean 	Is the mod available for search. This can be false when a mod is experimental, in a deleted state or has only alpha files
thumbsUpCount 	integer(int32) 	The mod's thumbs up count
"""

# Mod Class
class Mod(object):
    def __init__(self, id: int, gameId: int, name: str, slug: str, links: ModLinks, summary: str, status: ModStatus, downloadCount: int, isFeatured: bool, primaryCategoryId: int, categories: list[Category], authors: list[ModAuthor], logo: ModAsset, screenshots: list[ModAsset], mainFileId: int, latestFiles: list[File], latestFilesIndexes: list[FileIndex], dateCreated: datetime, dateModified: datetime, dateReleased: datetime, gamePopularityRank: int, isAvailable: bool, thumbsUpCount: int, classId: int|None = None, allowModDistribution: bool|None = None):
        self.id: int = int(id)
        self.gameId: int = int(gameId)
        self.name: str = str(name)
        self.slug: str = str(slug)
        self.links: ModLinks = ModLinks(**links) if isinstance(links, dict) else links
        self.summary: str = str(summary)
        self.status: ModStatus = ModStatus(status)
        self.downloadCount: int = int(downloadCount)
        self.isFeatured: bool = bool(isFeatured)
        self.primaryCategoryId: int = int(primaryCategoryId)
        self.categories: list[Category] = list(map(lambda i: Category(**i) if isinstance(i, dict) else i, categories))
        self.classId: int|None = int(classId) if classId else None
        self.authors: list[ModAuthor] = list(map(lambda i: ModAuthor(**i) if isinstance(i, dict) else i, authors))
        self.logo: ModAsset = ModAsset(**logo) if isinstance(logo, dict) else logo
        self.screenshots: list[ModAsset] = list(map(lambda i: ModAsset(**i) if isinstance(i, dict) else i, screenshots))
        self.mainFileId: int = int(mainFileId)
        self.latestFiles: list[File] = list(map(lambda i: File(**i) if isinstance(i, dict) else i, latestFiles))
        self.latestFilesIndexes: list[FileIndex] = list(map(lambda i: FileIndex(**i) if isinstance(i, dict) else i, latestFilesIndexes))
        self.dateCreated: datetime = datetime.strptime(dateCreated, "%Y-%m-%dT%XZ") if isinstance(dateCreated, str) else dateCreated
        self.dateModified: datetime = datetime.strptime(dateModified, "%Y-%m-%dT%XZ") if isinstance(dateModified, str) else dateModified
        self.dateReleased: datetime = datetime.strptime(dateReleased, "%Y-%m-%dT%XZ") if isinstance(dateReleased, str) else dateReleased
        self.allowModDistribution: bool|None = bool(allowModDistribution) if allowModDistribution is not None else None
        self.gamePopularityRank: int = int(gamePopularityRank)
        self.isAvailable: bool = bool(isAvailable)
        self.thumbsUpCount: int = int(thumbsUpCount)

# ModAsset Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
modId 	integer(int32) 	none
title 	string 	none
description 	string 	none
thumbnailUrl 	string 	none
url 	string 	none
"""

# ModAsset Class
class ModAsset(object):
    def __init__(self, id: int, modId: int, title: str, description: str, thumbnailUrl: str, url: str):
        self.id: int = int(id)
        self.modId: int = int(modId)
        self.title: str = str(title)
        self.description: str = str(description)
        self.thumbnailUrl: str = str(thumbnailUrl)
        self.url: str = str(url)

# ModAuthor Schema
"""
Properties
Name 	Type 	Description
id 	integer(int32) 	none
name 	string 	none
url 	string 	none
"""

# ModAuthor Class
class ModAuthor(object):
    def __init__(self, id: int, name: str, url: str):
        self.id: int = int(id)
        self.name: str = str(name)
        self.url: str = str(url)

# ModLinks Schema
"""
Properties
Name 	Type 	Description
websiteUrl 	string 	none
wikiUrl 	string 	none
issuesUrl 	string 	none
sourceUrl 	string 	none
"""

# ModLinks Class
class ModLinks(object):
    def __init__(self, websiteUrl: str, wikiUrl: str, issuesUrl: str, sourceUrl: str):
        self.websiteUrl: str = str(websiteUrl)
        self.wikiUrl: str = str(wikiUrl)
        self.issuesUrl: str = str(issuesUrl)
        self.sourceUrl: str = str(sourceUrl)

# ModLoaderInstallMethod Schema
"""
Possible enum values:

1=ForgeInstaller

2=ForgeJarInstall

3=ForgeInstaller_v2
"""

# ModLoaderInstallMethod Enum
class ModLoaderInstallMethod(enum.Enum):
    ForgeInstaller = 1
    ForgeJarInstall = 2
    ForgeInstaller_v2 = 3

# ModLoaderType Schema
"""
Possible enum values:

0=Any

1=Forge

2=Cauldron

3=LiteLoader

4=Fabric

5=Quilt
"""

# ModLoaderType Enum
class ModLoaderType(enum.Enum):
    Any = 0
    Forge = 1
    Cauldron = 2
    LiteLoader = 3
    Fabric = 4
    Quilt = 5

# ModSearchSortField Schema
"""
Possible enum values:

1=Featured

2=Popularity

3=LastUpdated

4=Name

5=Author

6=TotalDownloads

7=Category

8=GameVersion
"""

# ModSearchSortField Enum
class ModSearchSortField(enum.Enum):
    Featured = 1
    Popularity = 2
    LastUpdated = 3
    Name = 4
    Author = 5
    TotalDownloads = 6
    Category = 7
    GameVersion = 8

# ModStatus Schema
"""
Possible enum values:

1=New

2=ChangesRequired

3=UnderSoftReview

4=Approved

5=Rejected

6=ChangesMade

7=Inactive

8=Abandoned

9=Deleted

10=UnderReview
"""

# ModStatus Enum
class ModStatus(enum.Enum):
    New = 1
    ChangesRequired = 2
    UnderSoftReview = 3
    Approved = 4
    Rejected = 5
    ChangesMade = 6
    Inactive = 7
    Abandoned = 8
    Deleted = 9
    UnderReview = 10

# Pagination Schema
"""
Properties
Name 	Type 	Description
index 	integer(int32) 	A zero based index of the first item that is included in the response
pageSize 	integer(int32) 	The requested number of items to be included in the response
resultCount 	integer(int32) 	The actual number of items that were included in the response
totalCount 	integer(int64) 	The total number of items available by the request
"""

# Pagination Class
class Pagination(object):
    def __init__(self, index: int, pageSize: int, resultCount: int, totalCount: int):
        self.index: int = int(index)
        self.pageSize: int = int(pageSize)
        self.resultCount: int = int(resultCount)
        self.totalCount: int = int(totalCount)

# SearchModsResponse Schema
"""
Properties
Name 	Type 	Description
data 	[Mod] 	The response data
pagination 	Pagination 	The response pagination information
"""

# SearchModsResponse Class
class SearchModsResponse(object):
    def __init__(self, data: list[Mod], pagination: Pagination):
        self.data: list[Mod] = list(map(lambda x: Mod(**x) if isinstance(x, dict) else x, data))
        self.pagination: Pagination = Pagination(**pagination) if isinstance(pagination, dict) else pagination

# SortableGameVersion Schema
"""
Properties
Name 	Type 	Description
gameVersionName 	string 	Original version name (e.g. 1.5b)
gameVersionPadded 	string 	Used for sorting (e.g. 0000000001.0000000005)
gameVersion 	string 	game version clean name (e.g. 1.5)
gameVersionReleaseDate 	string(date-time) 	Game version release date
gameVersionTypeId 	integer(int32)¦null 	Game version type id
"""

# SortableGameVersion Class
class SortableGameVersion(object):
    def __init__(self, gameVersionName: str, gameVersionPadded: str, gameVersion: str, gameVersionReleaseDate: str, gameVersionTypeId: int|None = None):
        self.gameVersionName: str = str(gameVersionName)
        self.gameVersionPadded: str = str(gameVersionPadded)
        self.gameVersion: str = str(gameVersion)
        self.gameVersionReleaseDate: str = str(gameVersionReleaseDate)
        self.gameVersionTypeId: int|None = int(gameVersionTypeId) if gameVersionTypeId is not None else None


# SortOrder Class
class SortOrder(enum.Enum):
    Ascending = "asc"
    Descending = "desc"

# StringResponse Schema
"""
Properties
Name 	Type 	Description
data 	string 	The response data
"""

# StringResponse Class
class StringResponse(object):
    def __init__(self, data: str):
        self.data: str = str(data)

# ApiResponseCodes Class
class ApiResponseCode(enum.Enum):
    OK = 200
    Created = 201
    Accepted = 202
    NoContent = 204
    BadRequest = 400
    Unauthorized = 401
    Forbidden = 403
    NotFound = 404
    MethodNotAllowed = 405
    NotAcceptable = 406
    Conflict = 409
    Gone = 410
    UnprocessableEntity = 422
    TooManyRequests = 429
    InternalServerError = 500
    NotImplemented = 501
    BadGateway = 502
    ServiceUnavailable = 503
    GatewayTimeout = 504
#endregion
