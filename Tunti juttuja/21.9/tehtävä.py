class Muoto:
    def __init__(self, vari):
        self.vari = vari

    def mittaa(x):
        print(f'Piiri: ...')


class Suorakulmio(Muoto):
    def __init__(self, vari, pituus, leveys):
        self.pituus = pituus
        self.leveys = leveys
        super().__init__(vari)

    def mittaa(self):
        super().mittaa()
        piiri = 2 * (self.leveys + self.pituus)
        print(f'Piiri on {piiri}')

s1 = Suorakulmio('Punainen', 3, 4)
s1.mittaa()