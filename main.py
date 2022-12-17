# write an api to interact with the curseforge api
# https://docs.curseforge.com/?python=#getting-started


from CFAPI import CFAPI
from internalTools.env import CF_API
import SchemaClasses as schemas

cf = CFAPI(CF_API)

#test_get_games = cf.get_games()
#test_get_game = cf.get_game(432)
#test_get_versions = cf.get_versions(432)
#test_get_version_types = cf.get_version_types(432)
#test_get_categories = cf.get_categories(432)
#test_search_mods = cf.search_mods(432)
#test_get_mod = cf.get_mod(729219)
#test_get_mods = cf.get_mods([729219])
#featured_mods_search = schemas.GetFeaturedModsRequestBody(432, [], 73242)
#test_get_featured_mods = cf.get_featured_mods(featured_mods_search)
#test_get_mod_description = cf.get_mod_description(729219)
#test_get_mod_file = cf.get_mod_file(729219, 4159320)
#test_get_mod_files = cf.get_mod_files(729219)
#test_get_files = cf.get_files(schemas.GetModFilesRequestBody([0, 4159320]))
#test_get_mod_file_changelog = cf.get_mod_file_changelog(729219, 4159320)
#test_get_mod_file_download_url = cf.get_mod_file_download_url(729219, 4159320)
#test_get_fingerprints_matches = cf.get_fingerprints_matches(schemas.GetFingerprintMatchesRequestBody([2352728825]))
#test_get_fingerprints_fuzzy_matches = cf.get_fingerprints_fuzzy_matches(schemas.GetFuzzyMatchesRequestBody(432, [schemas.FolderFingerprint("test", [2352728825])]))
#test_get_minecraft_versions = cf.get_minecraft_versions()
#test_get_specific_minecraft_version = cf.get_specific_minecraft_version("1.16.5")
#test_get_minecraft_modloaders = cf.get_minecraft_modloaders()
#test_get_specific_minecraft_modloader = cf.get_specific_minecraft_modloader("Forge")
pass