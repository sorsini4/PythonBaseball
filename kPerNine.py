#Official player stats for 2020

players = [{
    'name': 'Clayton Kershaw',
    'IP': 58.1,
    'KS': 62
},
{
    'name': 'Gerrit Cole',
    'IP': 73,
    'KS': 94
},
{
    'name': 'Shane Bieber',
    'IP': 77.1,
    'KS': 122
}]

print("In 2020")

for player in players:
    name = player['name']
    ip = player['IP']
    k = player['KS']
    strikeout_per_9 = round((k/ip) * 9, 3)
    print(name + ' had a K per 9 of ' + str(strikeout_per_9))


