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

def create_datetime(date_string: str) -> datetime:
    # Find the index of "T"
    t_index = date_string.index("T")

    # Slice the string into its date and time parts
    date_part = date_string[:t_index]
    time_part = date_string[t_index+1:]

    # Split the date and time parts into their individual components
    year, month, day = date_part.split("-")
    hour, minute, second = time_part.split(":")
    second = second[0:2]

    # Parse the microseconds part if it is present
    if "." in time_part:
        dot_index = time_part.index(".")
        microseconds_part = time_part[dot_index+1:-1]
        date = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microseconds_part))
    else:
        date = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

    return date