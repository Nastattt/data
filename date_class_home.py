# from dataclasses import dataclass
#
#
# @dataclass
# class AirCastle:
#     height: int
#     blocks: int
#     color: str
#
#     def charge_height(self, value):
#         self.height = value if value > -1 else 0
#
#     def __add__(self, other):
#         if not isinstance(other, int):
#             raise TypeError('нужно целое число')
#         self.blocks = self.blocks + other
#         self.height = self.height + other // 5
#
#         return AirCastle
#

class GoodIfrit:
    def __init__(self, height, name, goodness):
        self.height = height
        self.name = name
        self.goodness = max(goodness, 0)  # Доброта не может быть отрицательной

    def change_goodness(self, value):
        self.goodness = max(self.goodness + value, 0)

    def __add__(self, number):
        return GoodIfrit(self.height + number, self.name, self.goodness)

    def __call__(self, argument):
        return argument * self.goodness // self.height

    def __str__(self):
        return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"

    def __lt__(self, other):
        if self.goodness != other.goodness:
            return self.goodness < other.goodness
        if self.height != other.height:
            return self.height < other.height
        return self.name < other.name

    def __gt__(self, other):
        return other.__lt__(self)

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return (self.goodness, self.height, self.name) == (other.goodness, other.height, other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

# Пример использования
gi1 = GoodIfrit(180, "Ifrit1", 5)
gi2 = GoodIfrit(170, "Ifrit2", 8)

print(gi1)
print(gi2)

gi1.change_goodness(-3)
print(gi1)

gi3 = gi1 + 10
print(gi3)

result = gi1(20)
print(result)

print(gi1 < gi2)
print(gi1 == gi3)



class Wizard:
    def __init__(self, name, rating, age_appearance):
        self.name = name
        self.rating = max(1, min(100, rating))
        self.age_appearance = max(1, age_appearance)

    def change_rating(self, value):
        self.rating = max(1, min(100, self.rating + value))
        age_change = abs(value) // 10
        if value > 0:
            self.age_appearance = max(1, self.age_appearance - age_change)
        elif value < 0:
            self.age_appearance += age_change
            if self.age_appearance > 18:
                self.age_appearance = 18

    def __iadd__(self, string):
        length = len(string)
        self.rating += length
        age_change = length // 10
        self.age_appearance = max(1, self.age_appearance - age_change)
        return self

    def __call__(self, argument):
        return (argument - self.age_appearance) * self.rating

    def __str__(self):
        return f'Wizard {self.name} with {self.rating} rating looks {self.age_appearance} years old'

    def __lt__(self, other):
        if self.rating != other.rating:
            return self.rating < other.rating
        if self.age_appearance != other.age_appearance:
            return self.age_appearance < other.age_appearance
        return self.name < other.name

    def __gt__(self, other):
        return other.__lt__(self)

    def __le__(self, other):
        return not self.__gt__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    def __eq__(self, other):
        return (self.rating, self.age_appearance, self.name) == (other.rating, other.age_appearance, other.name)

    def __ne__(self, other):
        return not self.__eq__(other)

# Пример использования
wd1 = Wizard('Gandalf', 90, 150)
wd2 = Wizard('Merlin', 80, 30)

print(wd1)
print(wd2)

wd1.change_rating(5)
print(wd1)

wd2 += 'magic'
print(wd2)

result = wd1(25)
print(result)

print(wd1 < wd2)
print(wd1 == wd2)



