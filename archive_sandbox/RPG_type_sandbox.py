
hp = 500

lvl = 1; dmg_border = 10


def dmg_calculated(dmg):
    global armor, hp
    hp -= dmg 

class CharStat:
    def __init__(self):
        self.dmg_border = 0

    def dmg_border_cal(self, lvl):
        self.dmg_border = lvl * 10

char = CharStat()
char.dmg_border_cal(lvl)

print(dmg_border)
