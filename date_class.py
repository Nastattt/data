from dataclasses import dataclass, field, InitVar,make_dataclass
from typing import Any
import random

class Tring:

    def __init__(self, name, weight, price, dims=[]):
        self.price = price
        self.weight = weight
        self.name = name
        self.dims = dims

    def __repr__(self):
        return f'{self.__dict__}'

    def __eq__(self, other):
        return self.price == other.price


# альтернатива выше
@dataclass
class ThingData:
    name: str
    weight: int
    price: float
    dims: list = field(default_factory=list)

    def __eq__(self, other):
        return self.price == other.price


th = Tring('name', 15, 150)
th.dims.append(10)
print(th)
print(th)
td2 = ThingData('name2', 12, 2.5)
print(th == td2)


class Vector3D:

    def __init__(self, x, y, z,calc_len:bool = True):
        self.z = z
        self.y = y
        self.x = x
        self.lenght = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if calc_len else 0



@dataclass
class VectorData:
    x: int = field(compare = False)
    y: int
    z: int
    length: float = field(init = False)
    pi : float = field(init = False)
    calc_len: InitVar[bool] = True

    def __post_init__(self, calc_len=None):
        if calc_len:
            self.lenght = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
        self.pi = 3.14

v = Vector3D(1,4,3)

print(v.__dict__)
vd = VectorData(1,2,3)

@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any
    weight: Any

    def __post_init__(self):
        print('Goods')
        Goods.current_uid += 1
        self.uid = Goods.current_uid

class GoodMeassureFactory:

    @staticmethod
    def get_init_meassure():
        return [0,0,0]



@dataclass
class Book(Goods):
    title:str
    author: str
    price:int
    weight :float
    meassure:list = field(default_factory = GoodMeassureFactory.get_init_meassure)

    def __post_init__(self):
        super().__post_init__()
        print('Book')

g = Goods('2434',1200)
print(g)
g1 = Goods('253',34)
print(g1)
b = Book(200,2.5,'dfgd','fhgf')

class Car:
    def __init__(self,model,max_speed,price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_Speed(self):
        return self.max_speed

@dataclass
class CarD:
    madel:str
    max_speed:int | float
    price: int = field(default=0)

    def det_max_speed(self):
        return self.max_speed

    def get_price(self):
        return self.price


CarData = make_dataclass('CarData',[('model',str),'max_speed',('price',int,field(default=0))],
                         namespace={'get_max_speed': lambda self:self.max_spped,
                                    'get_price':lambda self: self.price})
cd = CarData('Lfda Granta',120,45556667)
print(cd.get_max_speed())
print(cd.get_price())