from pybaseball import statcast_batter
from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher


hoskins_id = playerid_lookup('hoskins', 'rhys')
print(hoskins_id)

print("statcast stats from march 1st to april 1st")
hoskins_statcast = statcast_batter('2019-03-01', '2019-04-01', 656555)

print(hoskins_statcast)


"""
kersh = playerid_lookup('kershaw', 'clayton')

kershaw_stats = statcast_pitcher('2017-06-01', '2017-07-01', kersh)

print(kershaw_stats.head(5))
"""
