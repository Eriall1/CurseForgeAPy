# write an api to interact with the curseforge api
# https://docs.curseforge.com/?python=#getting-started


from CFAPI import CFAPI

import os
from env import CF_API

cf = CFAPI(CF_API)
