months = ('Kevät', 'Kesä', 'Syksy', 'Talvi')

x = int(input('Anna kuukausi numerona: \t'))

if x in (12, 1, 2):
    print(months[3])
elif x in (3, 4, 5):
    print(months[0])
elif x in (6, 7, 8):
    print(months[1])
elif x in (9, 10, 11):
    print(months[2])