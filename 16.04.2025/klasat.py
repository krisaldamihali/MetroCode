
class Personazhi():
    def __init__(self, emri, fuqia, shpejtesia):
        self.emri = emri
        self.fuqia = fuqia
        self.shpejtesia = shpejtesia

    def __str__(self):
        return f'{self.emri} {self.fuqia}'

    def stervitje(self):
        self.fuqia += 10
        self.shpejtesia += 15


armiku = Personazhi('Megatron', 98, 40)
i_miri = Personazhi('Pirro', 80, 90)

print(f'Armiku ka {armiku.fuqia} pike fuqie')
print(f'{i_miri.emri} ka {i_miri.shpejtesia} pike shpejtesie\n')

print(f'Armiku kishte {armiku.shpejtesia} pike shpejtesie')
# Armiku stervitet
armiku.stervitje()

print(f'Pasi u stervit armiku ka {armiku.shpejtesia} pike shpejtesie')

print(armiku)
