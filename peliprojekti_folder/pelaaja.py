class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, kohde):
        self.sijainti = kohde

    def keraa_esine(self):
        if self.sijainti.esine is not None:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(f'\nKeräsit esineen: {esine.nimi}')
        else: 
            print('\nTässä huoneessa ei ole esinettä.')