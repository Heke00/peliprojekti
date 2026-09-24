class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
 

auto1 = Auto('ABC-123', 142)

print(auto1.rekisteritunnus)
print(auto1.huippunopeus)
print(auto1.nopeus)
print(auto1.matka)