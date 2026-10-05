from pelaaja import Pelaaja
from huone import Huone
from esine import Esine
from teksti import nayta_intro, nayta_ohjeet, kirjoita_hitaasti
import time  # tuo eri tiedostoista luokat ja funktiot


def tallenna_peli(pelaaja, huoneet):
    with open("save.txt", "w", encoding="utf-8") as tiedosto:

        #Tallenna pelaajan nimi
        tiedosto.write(pelaaja.nimi + "\n")

        #Tallenna pelaajan sijainti
        tiedosto.write(pelaaja.sijainti.nimi + "\n")

        #Tallenna pelaajan tavrat reppuun
        tiedosto.write("REPPU\n")

        for esine in pelaaja.esineet:
            tiedosto.write(esine.nimi + "\n")

        # Tallenna huoneet ja niiden esineet
        tiedosto.write("HUONEET\n")

        for huone in huoneet:

            if huone.esine is not None: # jos ei ole tyhjä
                tiedosto.write(
                    huone.nimi + ":" + huone.esine.nimi + "\n"
                )
            else:
                tiedosto.write(
                    huone.nimi + ":None\n"  #jos tyhjä
                )


def lataa_peli(huoneet, esineet):
    try: # Try except mahdollisen errorin takia
        with open("save.txt", "r", encoding="utf-8") as tiedosto:
            rivit = tiedosto.read().splitlines()    # en oikein tiedä mitä se tekee mutta toimii

        #Lukee save.txt pelaajan nimi ja sijainti
        nimi = rivit[0]
        sijainti = rivit[1]

        # Pelaaja pistetään ekaan huoneeseen
        pelaaja = Pelaaja(nimi, huoneet[0])

        # Tarkistetaan missä pelaaja oli ja pistetään sinne
        for huone in huoneet:
            if huone.nimi == sijainti:
                pelaaja.sijainti = huone
                break

        # löydä save.txt repun ja huoneen kohta
        reppu_alku = rivit.index("REPPU") + 1
        huoneet_alku = rivit.index("HUONEET")

        # Tyhjennetään kaikkien huoneiden esineet
        for huone in huoneet:
            huone.esine = None

        # Luetaan repussa olevat tallennetut esineet
        for rivi in rivit[reppu_alku:huoneet_alku]:

            for esine in esineet:

                if esine.nimi == rivi: # jos se on tallennettu lisätään reppuun
                    pelaaja.esineet.append(esine)
                    break

        # Ladataan huoneissa olevat esineet
        for rivi in rivit[huoneet_alku + 1:]:

            huone_nimi, esine_nimi = rivi.split(":", 1)

            # Etsi huoneesi
            loytynyt_huone = None

            for huone in huoneet:
                if huone.nimi == huone_nimi:
                    loytynyt_huone = huone
                    break

            if loytynyt_huone is None:
                continue

            # Jos huoneessa ei ole esinettä:
            if esine_nimi == "None":
                loytynyt_huone.esine = None
                continue

            # Etsi oikea esine
            for esine in esineet:

                if esine.nimi == esine_nimi:
                    loytynyt_huone.esine = esine
                    break

        return pelaaja

    except FileNotFoundError:
        return None


nayta_intro()
input("Paina Enter jatkaaksesi...")

nayta_ohjeet()
input("Paina Enter jatkaaksesi...")


#Luodaan huoneet

keittio = Huone("Keittiö")
olohuone = Huone("Olohuone")
makuuhuone = Huone("Makuuhuone")
eteinen = Huone("Eteinen")
vessa = Huone("Vessa")
kellari = Huone("Kellari")
tyohuone = Huone("Työhuone")

# Kaikki huoneet listataan
huoneet = [
    keittio,
    olohuone,
    makuuhuone,
    eteinen,
    vessa,
    kellari,
    tyohuone
]


# Esineet


avain = Esine("Avain", 0.04)
kirja = Esine("Kirja", 0.4)
suurennuslasi = Esine("Suurennuslasi", 0.28)
taskulamppu = Esine("Taskulamppu", 0.35)
paristo = Esine("Paristo", 0.05)

# Kaikki esineet listataan
esineet = [
    avain,
    kirja,
    suurennuslasi,
    taskulamppu,
    paristo
]


#tavarat sijoitetaan halutuille paikoille

keittio.esine = avain
makuuhuone.esine = kirja
kellari.esine = taskulamppu
tyohuone.esine = suurennuslasi
olohuone.esine = paristo


#kokeile avata pelin tallennus

try:
    with open("save.txt", "r", encoding="utf-8"):
        tallennus_on = True

except FileNotFoundError:
    tallennus_on = False


# jos tallennus löytyy

if tallennus_on:

    while True: # looppi kunnes valitset y/n

        jatka = input(
            "\n\033[1;33mHaluatko jatkaa tallennettua peliä? (y/n): \033[0m"
        ).lower()

        if jatka == "y":

            pelaaja = lataa_peli( 
                huoneet,
                esineet
            )

            break

        elif jatka == "n":

            userName = input("\nMikä sinun nimesi on?:\t")
            pelaaja = Pelaaja(userName, keittio)

            break

        else:

            print(
                "\n\033[1;34mAnna vastaukseksi k tai e.\033[0m"
            )

else:

    userName = input("\nMikä sinun nimesi on?:\t")  
    pelaaja = Pelaaja(userName, keittio)


# gameloop

while True:

    print(
        "\n\033[1m-------------- peliprojekti by Heikki --------------\033[0m" # title
    )

    print()

    print(
        f"\033[1;32mOlet huoneessa: "       #kertoo missä olet
        f"{pelaaja.sijainti.nimi}\033[0m"
    )

    print()

    print("1. Katso huonetta")
    print("2. Kerää esine")
    print("3. Liiku")
    print("4. Katso reppu")                     #näyttää saatavat komennot
    print("5. Kuka olen?")
    print("6. Avaa etuovi")#tämä olisi kiva avata vasta kun on eteisessä, mutta en osaa
    print("7. Lopeta & tallenna")

    komento = input(
        "\n\033[1;33mValitse 1-7:\t\033[0m"
    )


 

    if komento == "1": # Tarkista esineet huoneessa

        if pelaaja.sijainti == eteinen:

            print(
                "\n\033[1;34mEteisessä on etuovi.\033[0m"       #erikois tapahtuma eteisessä
            )

        if pelaaja.sijainti == vessa:

            print(
                "\n\033[1;34mVessassa on pönttö. "         
                "Ei mitään hyödyllistä.\033[0m"
            )                                                   #erikois tapahtuma vessassa

        if pelaaja.sijainti.esine is not None:

            print(
                f"\n\033[1;34mHuoneessa on: "
                f"{pelaaja.sijainti.esine.nimi}\033[0m" 
            )                                                   # jos huoneessa on jotain:

        else:

            print(
                "\n\033[1;34mHuoneessa ei ole esinettä.\033[0m"
            )                                                           # else ei ole jotain:


  #kerää esine

    elif komento == "2":

        pelaaja.keraa_esine()


 # liiku 

    elif komento == "3":

        print(
            "\n\033[1;33mMihin haluat mennä?\033[0m\n"
        )

        for i, huone in enumerate(huoneet, 1):      #listaa kaikki huoneet ilman että joutuu pistämään kaikki tähän joka kerta

            print(
                f"{i}. {huone.nimi}"
            )

        kohde = input(
            "\n\033[1;33mValitse huone: \033[0m"
        )

        if kohde.isdigit():                     #jos se on int muodossa

            kohde = int(kohde)

            if 1 <= kohde <= len(huoneet):

                pelaaja.liiku(
                    huoneet[kohde - 1]
                )

            else:

                print(
                    "\n\033[1;34mVirheellinen valinta.\033[0m"
                )

        else:

            print(
                "\n\033[1;34mVirheellinen valinta.\033[0m"
            )


   # katso mitkä tavarat repussa

    elif komento == "4":

        if len(pelaaja.esineet) == 0:

            print(
                "\n\033[1;34mReppu on tyhjä.\033[0m"
            )   # jos reppu itemit = 0 

        else:

            print(
                "\n\033[1;34mRepussa on:\033[0m"
            )

            for esine in pelaaja.esineet:

                print(
                    f"- {esine.nimi}, "
                    f"{esine.paino} kg"
                ) #listaa esineet


   # vähän turha komento mutta näkee nimen ja voi tarkistaa toimiko tallennus

    elif komento == "5":

        print(
            f"\n\033[1;34mOlet {pelaaja.nimi}.\033[0m"
        )


# etuoven avaus 

    elif komento == "6":

        if pelaaja.sijainti == eteinen: # jos eteisessä

            if avain in pelaaja.esineet: # ja avain repussa

                print(
                    "\n\033[1;34mAvasit etuoven avaimella.\033[0m"
                )                                                       #outro

                print(
                    "\n\033[1;32mPääsit ulos!\033[0m"
                )

                time.sleep(0.5)

                kirjoita_hitaasti(
                    "\n\033[1;31m------------------ LOPPU ------------------\033[0m"
                )

                kirjoita_hitaasti(
                    "\n\033[1;31mOnneksi olkoon!\033[0m"
                )

                kirjoita_hitaasti(
                    "\033[1;31mLöysit avaimen ja pääsit turvallisesti ulos talosta.\033[0m"
                )

                kirjoita_hitaasti(
                    "\n\033[1;31mKiitos pelaamisesta, "
                    + pelaaja.nimi
                    + "!\033[0m"
                )

                break

            else:

                print(
                    "\n\033[1;34mEtuovi on lukossa. "
                    "Tarvitset avaimen.\033[0m"
                )

        else:

            print(
                "\n\033[1;34mTäällä ei ole etuovea.\033[0m"
            )


    # Pelin lopetus ja tallennus

    elif komento == "7":

        tallenna_peli(
            pelaaja,
            huoneet
        )              

        print(
            "\n\033[1;34mPeli tallennettu.\033[0m"
        )

        print(
            "\033[1;34mSuljetaan peli...\033[0m"
        )

        break # break the loop


  # jos valinta on joku muu kun sopiva:

    else:

        print(
            "\n\033[1;34mVirheellinen valinta.\033[0m"
        )