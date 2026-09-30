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

