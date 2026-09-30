class Hissi():

    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, x):
        while self.kerros < x and x <= self.ylin:
            self.kerros_ylös()
        if x < self.alin or x > self.ylin:
            print(f'{x}. Kerros ei olemassa')
    

        while self.kerros > x and x >= self.alin:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.kerros < self.ylin:
            self.kerros += 1
        else:
            print('Ei pysty. Ylin kerros jo')


    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros -= 1
        else:
            print('Ei pysty. Alin kerros jo')

hissi1 = Hissi(1, 7)



print(hissi1.kerros)

hissi1.kerros_ylös()

print(hissi1.kerros)




class Talo:

    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []

        for i in range(hissien_maara):
            hissi = Hissi(alin, ylin)
            self.hissit.append(hissi)

    def aja_hissia(self, numero, kohde):
        self.hissit[numero - 1].siirry_kerrokseen(kohde)
    
    def palohalytys(self):
        for i in self.hissit:
            i.siirry_kerrokseen(1)

talo1 = Talo(1, 10, 2)
print(f'Hissit: {len(talo1.hissit)}')

talo1.aja_hissia(1, 10)
talo1.aja_hissia(2, 7)
for i in talo1.hissit:
    print(f'Hissi on {i.kerros}. kerroksessa!')

talo1.palohalytys()
print('\n**Palohalytys**\n')

for i in talo1.hissit:
    print(f'Hissi on {i.kerros}. kerroksessa!')

