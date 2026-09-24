import random


class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0
    def kiihdyta(self, x):
        self.nopeus += x
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, x):
        self.matka += self.nopeus * x


autot = []

for i in range(1, 11):
    auto = Auto(f"ABC-{i}", random.randint(100, 200))
    autot.append(auto)


race = True

while race:

    for i in autot:
        i.kiihdyta(random.randint(-10, 15))

    for i in autot:
        i.kulje(1)

    for i in autot:
        if i.matka >= 10000:
            race = False
            print(f'{i.rekisteritunnus} voitti')
            break


print("Rekisteritunnus / Huippunopeus / Nopeus / Matka")
print("-----------------------------------------------")

for i in autot:
    print(f"{i.rekisteritunnus}\t{i.huippunopeus}\t{i.nopeus}\t{i.matka}\t")