class Viesti:
    lahetetty = 0
    def __init__(self, sisalto):
        self.sisalto = sisalto
        Viesti.lahetetty += 1

v1 = Viesti('moi')
v2 = Viesti('Miten menee?')
v3 = Viesti('heihei')

print(Viesti.lahetetty)