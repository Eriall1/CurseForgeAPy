# write an api to interact with the curseforge api
# https://docs.curseforge.com/?python=#getting-started


from CFAPI import CFAPI
from internalTools.env import CF_API

cf = CFAPI(CF_API)

test_get_games = cf.get_games()
test_get_game = cf.get_game(432)
test_get_versions = cf.get_versions(432)
test_get_version_types = cf.get_version_types(432)
test_get_categories = cf.get_categories(432)
test_search_mods = cf.search_mods(432)
pass