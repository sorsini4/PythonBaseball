class Player:
    """
    __init__ is the constructor class, its called at object 
    Any code you want to run directly after instantiation should obvi be added here
    """
    def __init__(self, name, pos, hits, at_bats, slg, obp):
        self.name = name
        self.pos = pos
        self.hits = hits
        self.at_bats = at_bats
        self.slg = slg
        self.obp = obp

    def batting_average(self):
        return self.hits / self.at_bats

    def on_base_plus_slugging(self):
        return self.obp + self.slg

    def slash_line(self):
        print(format(self.batting_average(), '.3f') + '/' + format(self.obp, '.3f') + '/' + format(self.slg, '.3f'))  

    def hitting_stats(self):
        return {
            'batting average': self.batting_average(),
            'ops': self.ops()
        }

