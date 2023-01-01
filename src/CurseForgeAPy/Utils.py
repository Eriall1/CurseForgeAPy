from CFAPI import CurseForgeAPI
from SchemaClasses import FileReleaseType, ApiResponseCode
from datetime import datetime

def downloadFileFromURL(self: CurseForgeAPI, url: str, filename: str):
    r = self.csesh.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)
    return ApiResponseCode[r.status_code]

def downloadFileFromID(self: CurseForgeAPI, id: str, filename: str):
    return downloadFileFromURL(self.getFiles([id]).data[0]['downloadUrl'], filename)

def downloadFileFromModID(self: CurseForgeAPI, modID: str, filename: str):
    mod = self.getMod(modID)
    return downloadFileFromURL(mod.data['latestFiles'][0]['downloadUrl'], filename)

def downloadFileFromModIDVersion(self: CurseForgeAPI, modID: str, version: str, filename: str, releaseType: FileReleaseType = FileReleaseType.Release):
    """ Will only download the first file that matches the version and release type (None for any release type)"""
    mod = self.getMod(modID)
    for file in mod.data['latestFiles']:
        if version in file.gameVersions and (file.releaseType == releaseType or not releaseType):
            return downloadFileFromURL(file['downloadUrl'], filename)
    raise Exception('Version not found matching the given release type.')