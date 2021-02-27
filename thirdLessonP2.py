pitchers = [{
    'name': 'Clayton Kershaw',
    'IP': 58.1,
    'Ks': 62
},
{
    'name': 'Gerrit Cole',
    'IP': 73,
    'Ks': 94
},
{
    'name': 'Shane Bieber',
    'IP': 77.1,
    'Ks': 122
}]

def get_ks_per_nine(pitcher):
    if type(pitcher) is not dict:
        print('Incorrect data type!')
        return
    
    ip = pitcher['IP']
    ks = pitcher['Ks']

    k_per = 9 * (ks / ip)

    return k_per


kersh = pitchers[-1]
bieber = pitchers[2]
bieber = get_ks_per_nine(bieber)

print('Clayton Kershaw\'s K/9 in 2020 was: ', format(get_ks_per_nine(kersh), '.3f'))
print('Gerrit Cole\'s K/9 in 2020 was: ', format(get_ks_per_nine(pitchers[1]), '.3f'))
print('Shane Bieber\'s K/9 in 2020 was: ', format(bieber, '.3f'))

