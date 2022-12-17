# write an api to interact with the curseforge api
# https://docs.curseforge.com/?python=#getting-started


from CFAPI import CFAPI
from internalTools.env import CF_API
import SchemaClasses as schemas

cf = CFAPI(CF_API)

test_get_games = cf.get_games()
test_get_game = cf.get_game(432)
test_get_versions = cf.get_versions(432)
test_get_version_types = cf.get_version_types(432)
test_get_categories = cf.get_categories(432)
test_search_mods = cf.search_mods(432)
test_get_mod = cf.get_mod(729219)
test_get_mods = cf.get_mods([729219, 729220])
featured_mods_search = schemas.GetFeaturedModsRequestBody(432, [], 73242)
test_get_featured_mods = cf.get_featured_mods(featured_mods_search)
pass