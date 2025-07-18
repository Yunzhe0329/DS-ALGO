#傳統的寫法，要一直寫 __init__ -> 麻煩 -> animal2.py 展示另一種寫法
class Animal:
    def __init__(self, color, leg_num):
        self.species = self.__class__.__name__
        self.color = color
        self.leg_num = leg_num
    def __repr__(self):
        return f'{self.species}(color={self.color!r}, leg_num={self.leg_num})'

class Elephant(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
class Zebra(Animal):
    def __init__(self, color):
        super().__init__(color, 4)
class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)
class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)

# 實作展示區類別
class Exhibit():
    def __init__(self, id_num):
        self.id_num = id_num
        self.animals = []
    def add_animals(self, *new_animals):
        for animal in new_animals:
            self.animals.append(animal)
    def __repr__(self):
        return f'展示區編號 : {self.id_num}:' + \
                f'{", ".join([str(animal) for animal in self.animals])}'

ex1 = Exhibit(1)
ex2 = Exhibit(2)

ex1.add_animals(Elephant('灰'), Zebra('黑白'))
ex2.add_animals(Snake('綠'), Parrot('灰'))
print(ex1)
print(ex2)

#實作動物園類別
class Zoo():
    def __init__(self):
        self.exhibits = []
    def add_exhibits(self, *new_exhibits):
        for exhibit in new_exhibits:
            self.exhibits.append(exhibit)
    def __repr__(self):
        return f'動物園：\n' + \
                '\n'.join([str(exhibit) for exhibit in self.exhibits])
    def animals_by_color(self, color):
        return [animal for exhibit in self.exhibits
                for animal in exhibit.animals
                if animal.color == color]
    def animal_by_leg_num(self, leg_num):
        return [animal
                for exhibit in self.exhibits
                for animal in exhibit.animals
                if animal.leg_num == leg_num]
    def animal_total_leg_num(self):
        return sum([animal.leg_num
                    for exhibit in self.exhibits
                    for animal in exhibit.animals])
zoo = Zoo()
zoo.add_exhibits(ex1, ex2)
print(zoo)
print('灰色動物數量 : ', zoo.animals_by_color('灰'))
print('4 條腿動物 :', zoo.animal_by_leg_num(4))
print('腿的總數 : ', zoo.animal_total_leg_num())