# CurseForgeAPy

[![GitHub issues](https://img.shields.io/github/issues/James2854/CurseForgeAPy?style=for-the-badge)](https://github.com/James2854/CurseForgeAPy/issues)
[![GitHub stars](https://img.shields.io/github/stars/James2854/CurseForgeAPy?style=for-the-badge)](https://github.com/James2854/CurseForgeAPy/stargazers)
[![GitHub license](https://img.shields.io/github/license/James2854/CurseForgeAPy?style=for-the-badge)](https://github.com/James2854/CurseForgeAPy)

CurseForgeAPy is a Python package that provides a wrapper for the CurseForge API / Eternal API. With CurseForgeAPy, you can easily access and interact with the API in your Python scripts and applications.

## Warning
The CurseForgeApi has changed since the creation of this wrapper, and I do not have the time to fix it.
If ANYONE would like to contribute it would be vey welcome :)
Otherwise, some methods may have issues, namely mod search. 
There are some quick fixes that can be done on a local copy:
- patch the Mod class to accept latestEarlyAccessFilesIndexes keyword
- patch the FileIndex class to modify the modLoader kwarg to be optional or remove it.

I do not have time to go through the API, especially when it was painful enough to work through undocumented functionality when initially creating the package.
Curse forge is really bad at documenting their api, and there is no record of changes I could find. Currently, the documentation matches the previous specifications, however there is undocumented changes.

## Installation

To install CurseForgeAPy, simply use pip:
```bash
pip install CurseForgeAPy
```

## Features
- Classes for each data structure in the API (found in SchemaClasses.py)
- Fully cached requests with an expiry of 60 minutes
- Easy access and interaction with the API in Python scripts and applications
- Functions for searching and retrieving data from the API
- Support for pagination when querying the API
- Error handling for API requests
- Support for all API endpoints and methods
- Parsing and manipulating API responses made easy through response classes
- All classes can be fully instantiated through dictionaries passed into the constructor

## Documentation

For full documentation of the CurseForge API, please see the official CurseForge API documentation at https://docs.curseforge.com/. Docstrings are also available for some functions, however complete docstring creation for all functions is ongoing.

## Usage

To use CurseForgeAPy, you will need to obtain an API key from CurseForge. You can do this by creating an account on CurseForge and requesting an API key from [the developer portal](https://console.curseforge.com/#/api-keys).

Once you have obtained an API key, you can use CurseForgeAPy as follows:

```python
from CurseForgeAPy import CurseForgeAPI

# Instantiate the CurseForgeAPy client
client = CurseForgeAPI('YOUR_API_KEY')

# Use the client to make API requests
response = client.getGames() # -> returns a GetGamesResponse

print(response)
```

## Examples

Here are some examples of how you can use CurseForgeAPy to access and interact with the CurseForge API:

### Games
``` Python
# get all games
games = cf.getGames()

# get specific game
game = cf.getGame(432)

# get version of specific game
versions = cf.getVersions(432)

# get version type of specific game
versionTypes = cf.getVersionTypes(432)

# get all mod categories of specific game
categories = cf.getCategories(432)
```

### Mods
``` Python
import CurseForgeAPy.SchemaClasses as schemas

# search for mods within specific game
searchResults = cf.searchMods(432)

# get specific mod
mod = cf.getMod(729219)

# get an array of mods from ids
mods = cf.getMods([729219])

# initialise GetFeaturedModsRequestBody object for use in get_featured_mods
featuredModsSearch = schemas.GetFeaturedModsRequestBody(432, [], 73242)

# get featured mods within specific game
featuredMods = cf.GetFeaturedMods(featuredModsSearch)

# get string description of specific mod
modDescription = cf.getModDescription(729219)

# get specific file within specific mod
modFile = cf.getModFile(729219, 4159320)

# get files based off of FileId
modFiles = cf.getModFiles(729219)
```

### Files
``` Python
# get files from list of ids
files = cf.getFiles(schemas.GetModFilesRequestBody([4159320]))

# get changelog of a specified mod and file id
changelog = cf.getModFileChangelog(729219, 4159320)

# get download url for a mod file
modFileDownloadUrl = cf.getModFIleDownloadUrl(729219, 4159320)
```

### Fingerprints
``` Python
# get exact matches for a fingerprint
fingerprintsMatches = cf.getFingerprintsMatches(schemas.GetFingerprintMatchesRequestBody([2352728825]))

# get fuzzy matches for a partial fingerprint
fuzzyMatches = cf.getFingerprintsFuzzyMatches(schemas.GetFuzzyMatchesRequestBody(432, [schemas.FolderFingerprint("test", [2352728825])]))

```
### Minecraft
``` Python
# get minecraft versions
minecraftVersions = cf.getMinecraftVersions()

# get a specific minecraft version
minecraftVersion = cf.getSpecificMinecraftVersion("1.16.5")

# get a list of minecraft modloaders
minecraftModloaders = cf.getMinecraftModloaders()

# get a specific minecraft modloader
minecraftModloader = cf.getSpecificMinecraftModloader("forge-1.16.5-36.1.0")
```

### Utilities
``` Python
# Within the CurseForgeAPy package, there is a utility class that has a couple helper functions, mainly downloading files related.
# These functions shouldnt be called without a CurseForgeAPy client object, as they use the client to get the download url.

from CurseForgeAPy import Utils
from CurseForgeAPy import SchemaClasses as schemas

# Each function take in a CurseForgeAPy client object, and a specific parameter, finishing with a file path to save the file to.
cf = CFAPI('YOUR-API-KEY')

# Download a file from a url
Utils.downloadFileFromURL(cf, "file-url", "file-path")

# Download a specified file from id
Utils.downloadFileFromID(cf, 111111, "file-path")

# Download a specified file from a mod id
Utils.downloadFileFromModID(cf, 111111, "file-path")

# Download a specified file from a mod id and file id
Utils.downloadFileFromModIDAndFileID(cf, 111111, 222222, "file-path")

# Download a specified file from a mod id and version, with optional release type (defaults to None which is any release type)
# Can return an exception if the version is not found
Utils.downloadFileFromModIDVersion(cf, 111111, "1.16.5", "file-path", schemas.ReleaseType.Release)
```

## Support

If you have any issues or questions while using CurseForgeAPy, please feel free to open an issue on the GitHub repository or contact us through our support channels.

## Contribution

We welcome contributions to CurseForgeAPy! Please feel free to open a pull requests or issue if you would like a new feature.
