class Reaper():
    def __init__(self):
        self.size = 20
        self.hostile = True
        self.patrol = True
        self.aggro = False
        
    def set_aggro(self, player):
        print(f'Reaper is aggro towards {player} {self.aggro} > {not self.aggro}')

    def check_properties(self, player):
        print(f"Reaper is aggroed on player? {self.aggro}")
        print(f"Reaper is patrolling? {self.patrol}")

r = Reaper()
r.set_aggro('Johno')
