# library = [b1, b2, b3, b4]
# library.sort(key=lambda book: book.pages)
# for book in library:
#     print(f'Title: {book.title}, Pages: {book.pages}')



class Book:
    def __init__(self, author, title, pages=100):
        self.author = author
        self.title = title
        self.pages = pages

b1 = Book('K1', '04', 25)
b2 = Book('K2', '03')
b3 = Book('K3', '02', 27)
b4 = Book('K4', '01', 100)





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print(f'{self.name} kävelee')

    def is_adult(self):
        if self.age < 18:
            print(f'{self.name} ei ole aikuinen')
        else:
            print(f'{self.name} on aikuinen')

p1 = Person('James', 45)

print(b2.pages)