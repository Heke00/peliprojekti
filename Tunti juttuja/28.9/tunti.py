# with open("aaa.txt", "r") as f:
#     luettu = f.read()
#     print(luettu)


# with open('save2.txt', "a") as f:
#     for i in range(1, 51):
#         f.write(f'Moi {i}. kertaa\n')
        



# import json

# tallennus_data = {
#     "pelaaja" : "Matti",
#     "taso" : 5,
#     "varusteet" : ["miekka", "kilpi", "haarniska"]
# }

# with open('save.json', 'w') as tiedosto:
#     json.dump(tallennus_data, tiedosto)

# with open('save.json', 'r') as tiedosto:
#     data_luettu = json.load(tiedosto)

# print(f'Pelaaja: {data_luettu['pelaaja']}, taso: {data_luettu['taso']}, Varusteet: {data_luettu['varusteet']}')


# import os
# if os.path.exists("save.txt"):
#     os.remove('save.txt')
# else:
#     print('Tiedostoa ei löydy')

import json

li1 = [2, 6, "hello", (3, 4), [5, 6]]

with open('t1.json', 'w') as f:
    json.dump(li1, f)

# with open('t2.py', 'w') as f:


# with open('t2.py', 'x') as f:
#     f.write()