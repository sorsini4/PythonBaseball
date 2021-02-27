players = [{
    'name': 'CLayton Kershaw',
    'IP': 58.1,
    'hits': 41,
    'runs': 14,
    'k': 62
},
{
    'name': 'Gerrit Cole',
    'IP': 73,
    'hits': 53,
    'runs': 23,
    'k': 94
}]

def calc_fantasy_points(player):
    return player.get('IP', 0) * 3 - player.get('hits', 0) - player.get('runs', 0) * 2 + player.get('k', 0)

fantasy_points = [calc_fantasy_points(player) for player in players]

avg_fantasy_points = sum(fantasy_points)/len(fantasy_points)

print(avg_fantasy_points)
