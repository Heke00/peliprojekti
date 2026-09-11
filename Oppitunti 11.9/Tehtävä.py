# li = [2, 3, 2, 6, 7, 3, 3]


# x = set(li)
# print(list(x))


# hedelmät = {'Omena', 'Appelsiini', 'Vesimeloni'}
# print('Omena' in hedelmät)
 


students = [
    {"name": "Ella", "age": 14, "grade": "9"},
    {"name": "Leo", "age": 15, "grade": "8"},
    {"name": "Aino", "age": 14, "grade": "10"},
]

for i in students:
    print(f'{i['name']} on {i['age']} vuotta vanha ja hänen arvosanansa on {i['grade']}')

