# class Teacher:
#     def __init__(self, nimi):
#         self.nimi = nimi
#     def mun_stu(self, x):
#         print(f'Minä olen {self.nimi} ja oppilaani on {x.nimi}.')

# class Student:
#     def __init__(self, nimi):
#         self.nimi = nimi

# op1 = Teacher('Ari')
# opis1 = Student('Superman')

# op1.mun_stu(opis1)




# class Kirja:
#     def __init__(self, nimi, kirjailija):
#         self.nimi = nimi
#         self.kirjailija = kirjailija
# class Kirjailija:
#     def __init__(self, nimi):
#         self.nimi = nimi
    

# kirja = Kirja('AA', 'Matti')
# kirja2 = Kirja('BB', 'Mikko')
# kirjailija1 = Kirjailija('Matti')
# kirjailija2 = Kirjailija('Mikko')

# print(kirja.nimi)
# print(kirjailija1.kirjailija.nimi)
# print(kirja2.nimi)
# print(kirjailija2.nimi)


class Kaupunki:
    def __init__(self, nimi, asukas):
        self.nimi = nimi
        self.asukas = asukas
    def kuka(self):
        print(f'Asukas {self.asu.nimi} asuu {self.nimi}')

class Asukas:
    def __init__(self, nimi):
        self.nimi = nimi



asu1 = Asukas('Heikki')
asu2 = Asukas('Matti')

k1 = Kaupunki('Espoo', asu1.nimi)
k2 = Kaupunki('Vantaa', asu2.nimi)

print(f'{k1.asukas} asuu {k1.nimi}')
print(f'{k2.asukas} asuu {k2.nimi}')

kuka()