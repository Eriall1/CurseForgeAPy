# CurseForgeAPy

[![GitHub issues](https://img.shields.io/github/issues/James2854/CurseForgeAPy?style=for-the-badge)](https://github.com/James2854/CurseForgeAPy/issues)
[![GitHub stars](https://img.shields.io/github/stars/James2854/CurseForgeAPy?style=for-the-badge)](https://github.com/James2854/CurseForgeAPy/stargazers)
[![GitHub license](https://img.shields.io/github/license/James2854/CurseForgeAPy?style=for-the-badge)](https://github.com/James2854/CurseForgeAPy)

CurseForgeAPy is a Python package that provides a wrapper for the CurseForge API / Eternal API. With CurseForgeAPy, you can easily access and interact with the API in your Python scripts and applications. Currently, the entire API has been wrapped and each data structure has been reconstructed into seperate classes, which can be found within SchemaClasses.py.

## Installation

To install CurseForgeAPy, simply use pip:
```bash
pip install CurseForgeAPy
```

## Usage

To use CurseForgeAPy, you will need to obtain an API key from CurseForge. You can do this by creating an account on CurseForge and requesting an API key from [the developer portal](https://console.curseforge.com/#/api-keys).

Once you have obtained an API key, you can use CurseForgeAPy as follows:

```python
from CurseForgeAPy import CurseForgeAPI

# Instantiate the CurseForgeAPy client
client = CurseForgeAPI(api_key='YOUR_API_KEY')

# Use the client to make API requests
response = client.getGames() # -> returns a GetGamesResponse

print(response)
```

## Documentation

For full documentation of the CurseForge API, please see the official CurseForge API documentation at https://docs.curseforge.com/.

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
minecraftModloader = cf.getSpecificMinecraftModloader(0)
```

## TODO
- [ ] Implement the cache for requests
- [ ] Implement a file download method

## Support

If you have any issues or questions while using CurseForgeAPy, please feel free to open an issue on the GitHub repository or contact us through our support channels.

## Contribution

We welcome contributions to CurseForgeAPy! Please feel free to open a pull requests or issue if you would like a new feature.
