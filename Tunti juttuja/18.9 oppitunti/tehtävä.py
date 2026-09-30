# class Tili:
#     def __init__(self, saldo):
#         self.saldo = saldo
    
#     def talletus(self, maara):
#         self.saldo = self.saldo + maara
#     def nosto(self, maara):
#         self.saldo = self.saldo - maara


# t1 = Tili(200)
# t2 = Tili(1000)

# t1.talletus(50)
# t1.nosto(60)

# t2.talletus(10)
# t2.nosto(1000)

# print(t1.saldo)
# print(t2.saldo)


class Kirja:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirjasto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kirjat = []
    def lisaa(self, kirja):
        self.kirjat.append(kirja)


k1 = Kirja('Maila')
k2 = Kirja('Tuntematon sotilas')
k3 = Kirja('Aakkoset')
k4 = Kirja('Raamattu')

kir1 = Kirjasto('Oodi')

kir1.lisaa(k1)
kir1.lisaa(k2)

for i in kir1.kirjat:
    print(i.nimi)