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


def get_batting_average(player):
    if type(player) is not dict:
        print('You need to pass in a dictonary')
        return
    else:
        pass

    hits = player['hits']
    at_bats = player['at_bats']

    if hits > at_bats:
        print('You can not have more hits than at bats!')
        return
    else:
        pass

    batting_average = hits / at_bats
    
    return batting_average


trout = players[1]
trout_ba = get_batting_average(trout)
print('Trouts batting average: ', format(trout_ba, '.3f'))
print('Bellingers batting average: ', format(get_batting_average(players[0]), '.3f'))
print('Yelichs batting average: ',  format(get_batting_average(players[2]), '.3f'))
