class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdyta(self, x):
        self.nopeus += x
 

auto1 = Auto('ABC-123', 142)

print(f'Rek. tunnus: {auto1.rekisteritunnus}')
print(f'Huippunopeus: {auto1.huippunopeus} km/h')
print(f'Tämänhetkinen nopeus {auto1.nopeus} km/h')
print(f'Kuljettu matka: {auto1.matka} km')

print()


Auto.kiihdyta(auto1, 30)
Auto.kiihdyta(auto1, 70)
Auto.kiihdyta(auto1, 50)
print(f'{auto1.nopeus} km/h')
Auto.kiihdyta(auto1, -200)
print(f'{auto1.nopeus} km/h')

print()

