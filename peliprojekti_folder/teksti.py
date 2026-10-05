import os
import time


def kirjoita_hitaasti(teksti, nopeus=0.03):
    for kirjain in teksti:
        print(kirjain, end="", flush=True)
        time.sleep(nopeus)
    print()

def kirjoita_nopeasti(teksti, nopeus=0.01):
    for kirjain in teksti:
        print(kirjain, end="", flush=True)
        time.sleep(nopeus)
    print()


def nayta_intro():
    kansio = os.path.dirname(os.path.abspath(__file__))
    tiedosto = os.path.join(kansio, "intro.txt")

    with open(tiedosto, "r", encoding="utf-8") as tiedosto:
        teksti = tiedosto.read()

    print(teksti)


def nayta_ohjeet():
    kansio = os.path.dirname(os.path.abspath(__file__))
    tiedosto = os.path.join(kansio, "ohjeet.txt")

    with open(tiedosto, "r", encoding="utf-8") as tiedosto:
        teksti = tiedosto.read()

    print(teksti)
