from steam import Steam
from decouple import config

from data import myData
import pprint
import datetime


# KEY = config("STEAM_API_KEY")
# steam = Steam(KEY)
#
# result = steam.users.search_user("mickdiggin")
#
# pprint.pprint

# timecreated = datetime.date.fromtimestamp(myData['player']['timecreated'])
# print(timecreated)

KEY = config("STEAM_API_KEY")


steam = Steam(KEY)

# arguments: steamid
recentlyPlayed = steam.users.get_user_recently_played_games(myData['player']['steamid'])

pprint.pprint(recentlyPlayed)