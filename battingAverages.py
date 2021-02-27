#Official player stats for 2019

#these are dictonaries
players = [{
    'name': 'Cody Bellinger',
    'hits': 170,
    'at_bats': 558
},
{
    'name': 'Mike Trout',
    'hits': 137,
    'at_bats': 470
},
{
    'name': 'Christian Yelich',
    'hits': 161,
    'at_bats': 489
}]

print('In 2019:')

for player in players:
    name = player["name"]
    hits = player["hits"]
    at_bats = player["at_bats"]
    batting_average = round(hits/at_bats, 3)
    print(name + ' had a batting average of ' + str(batting_average))
