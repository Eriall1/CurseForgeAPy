# write an api to interact with the curseforge api
# https://docs.curseforge.com/?python=#getting-started

from CFAPI import CFAPI
import os

myparam = 'a'

my_secret = os.environ['CF_API_KEY']

cf = CFAPI(my_secret)

cf.get_games()
