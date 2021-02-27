import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pybaseball as pyb
from pybaseball import statcast_batter
from pybaseball import playerid_lookup 

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("chained_assignment", None)


pitchers_2018 = pyb.pitching_stats(2018)
pitchers_2019 = pyb.pitching_stats(2019)
pitchers_2020 = pyb.pitching_stats(2020)

df_2018 = pyb.batting_stats(2018)
df_2019 = pyb.batting_stats(2019)
df_2020 = pyb.batting_stats(2020)

#cards_df = df_2019.loc[df_2019['Team'] == "Cardinals"]
#cards_pitchers = pitchers_2019.loc[pitchers_2019['Team'] == "Cardinals"]
"""
winker_stats = statcast_batter('2020-08-01', '2020-08-03', 608385)
print(winker_stats)
"""

"""
Sorting the Cardinals (2019) by WAR (top 30)
And ONLY showing the WAR and name columns.
"""
#print(cards_df.sort_values(by = 'WAR', ascending = False).head(30))
#print(cards_pitchers)
#cards_df = cards_df.loc[cards_df['AB'] > 100]
#print(cards_df.loc[:, ['Name', 'WAR', 'Clutch', 'wRC+', 'Spd']].sort_values(by = 'wRC+', ascending = False).head(30))

#hoskins_df = df_2019.loc[df_2019['Name'] == 'Rhys Hoskins']
"""
This will print the specified stats for Rhys Hoskins only
print(hoskins_df.loc[:, ['Name', 'WAR', 'Clutch', 'wRC+', 'Spd']])
The next one on line 28 will print all stats for Rhys Hoskins
"""
#print(hoskins_df)

"""
This wil print the top 50 players in order of Hard%, along with showing a couple of other useful statistics
"""

"""
print('2018 hard hit % rankings top 150')
hhperc_df_2018 = df_2018.loc[df_2018['AB'] > 100]
print(hhperc_df_2018.loc[:, ['Name', 'Hard%', 'wRC+', 'HR', 'SLG']].sort_values(by = 'Hard%', ascending = False).head(150))

print('2019 hard hit % rankings top 150')
hhperc_df_2019 = df_2019.loc[df_2019['AB'] > 100]
print(hhperc_df_2019.loc[:, ['Name', 'Hard%', 'wRC+', 'HR', 'SLG']].sort_values(by = 'Hard%', ascending = False).head(150))

print('2020 hard hit % rankings top 150')
hhperc_df_2020 = df_2020.loc[df_2020['AB'] > 100]
print(hhperc_df_2020.loc[:, ['Name', 'Hard%', 'wRC+', 'HR', 'SLG']].sort_values(by = 'Hard%', ascending = False).head(150))

print('2019 slash lines, with ops @ end')
slash_df_2019 = df_2019.loc[df_2019['AB'] > 100]
print(slash_df_2019.loc[:, ['Name', 'AVG', 'OBP', 'SLG', 'OPS', 'HR', 'AB']].sort_values(by = 'OPS', ascending = False).head(100))
"""

#Jesse Winker wins this, along with Happ and KB as 2nd placers 
fantasy_players = ['Kris Bryant', 'Anthony Santander', 'Jorge Polanco', 'Ian Happ', 'Jesse Winker']
"""
print('2018 stats')
for player_name18 in fantasy_players:
    player18 = df_2018.loc[df_2018['Name'] == player_name18]    
    print(player18.loc[:, ['Name', 'Hard%', 'wRC+', 'HR', 'RBI', 'OPS', 'BB']].sort_values(by = 'OPS', ascending = False))

print('2019 stats')
for player_name19 in fantasy_players:
    player19 = df_2019.loc[df_2019['Name'] == player_name19]
    print(player19.loc[:, ['Name', 'Hard%', 'wRC+', 'HR', 'RBI', 'OPS', 'BB']].sort_values(by = 'OPS', ascending = False))

print('2020 stats')
for player_name20 in fantasy_players:
    player20 = df_2020.loc[df_2020['Name'] == player_name20]
    print(player20.loc[:, ['Name', 'Hard%', 'wRC+', 'HR', 'RBI', 'OPS', 'BB']].sort_values(by = 'OPS', ascending = False))
"""

"""
fantasy_players = ['Kris Bryant', 'Anthony Santander', 'Jorge Polanco', 'Ian Happ', 'Jesse Winker']
for player_name18 in fantasy_players:
    player18 = df_2018.loc[df_2018['Name'] == player_name18]    
    print(player18.loc[:, ['Name', 'wOBA', 'ISO', 'BABIP', 'AVG', 'OPS', 'AB']].sort_values(by = 'OPS', ascending = False))
 
print('2019 stats')
for player_name19 in fantasy_players:
    player19 = df_2019.loc[df_2019['Name'] == player_name19]
    print(player19.loc[:, ['Name', 'wOBA', 'ISO', 'BABIP', 'AVG', 'OPS', 'AB']].sort_values(by = 'OPS', ascending = False))
"""

"""
print('2020 stats')
for player_name20 in fantasy_players:
    player19 = df_2019.loc[df_2019['Name'] == player_name20]
    babip19 = player19['BABIP'].astype(float)
    player20 = df_2020.loc[df_2020['Name'] == player_name20]
    babip = player20['BABIP'].astype(float)
    print(player20.loc[:, ['Name', 'wOBA', 'ISO', 'BABIP', 'AVG', 'OPS', 'AB', {'BABIP increase': [(babip - )]} ]].sort_values(by = 'OPS', ascending = False))
"""


print("2020*********************************")
prospect_elig20 = df_2020.loc[df_2020['AB'] < 100]
print(prospect_elig20.loc[:, ['Name', 'AB', 'Age']].head(50))

"""
print("2019*********************************")
prospect_elig19 = df_2019.loc[df_2019['AB'] < 100]
print(prospect_elig19.loc[:, ['Name', 'AB', 'Age']])
"""

"""
pitchers = pitchers_2020.loc[pitchers_2020['IP'] < 50]
print(pitchers.loc[:, ['Name', 'IP', 'Age']].head(30))
"""



