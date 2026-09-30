ICAO = {
    "EFHK" : "Helsinki-Vantaan Lentoasema",
    "EFOU" : "Oulun Lentoasema",
    "EFRO" : "Rovaniemen Lentoasema",
    "EFKT" : "Kittilän Lentoasema",
    "EFIV" : "Ivalon Lentoasema",
    "EFKU" : "Kuopion Lentoasema",
    "EFVA" : "Vaasan Lentoasema",
    "EFTU" : "Turun Lentoasema",
    "EFTP" : "Tampere-Pirkkalan Lentoasema",
    "EFJO" : "Joensuun Lentoasema",
    "EFJY" : "Jyväskylän Lentoasema",
    "EFKI" : "Kajaanin Lentoasema",
    "EFKK" : "Kokkola-Pietarsaaren Lentoasema",
    "EFKS" : "Kuusamon Lentoasema",
    "EFKE" : "Kemi-Tornion Lentoasema",
    "EFMA" : "Maarianhaminan Lentoasema",
    "EFET" : "Enontekiön Lentoasema",
    "EFSA" : "Savonlinnan Lentoasema",
    "EFLP" : "Lappeenrannan Lentoasema"

}

while True:
    command = input('Komennot:\n\nSyötä uusi ICAO-koodi | "lisää" \nEtsi olemassa oleva lentoasema | "etsi" \nLopeta ohjelma | "lopeta"\nSyötä komento: \t')
    if command == "etsi":
        inpaico = input('Syötä ICAO-koodi: \t')
        if inpaico in ICAO:
            print(f"\n\033[1m{ICAO[inpaico]}\033[0m\n")
    elif command == "lisää":
        uusiiaco = input('Syötä uuden lentoaseman ICAO-koodi: \t')
        uusinimi = input('Syötä uuden lentoaseman nimi: \t ')
        ICAO[uusiiaco] = uusinimi
    elif command == "lopeta":
        print("suljetaan...")
        break