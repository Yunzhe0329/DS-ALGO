from dataclasses import dataclass
#dataclass 會自動實作__init__()和 __repr__()
@dataclass
class Animal:
    color : str
    leg_num : int

    def __post_init__(self): #@dataclass 會將你的參數全部放進__init__()，我們希望稍後再設定species 就可以實作 __post_init__()
        self.species = self.__class__.__name__
@dataclass
class Elephant(Animal):
    leg_num : int = 4
@dataclass
class Zebra(Animal):
    leg_num : int = 4

elephant = Elephant('灰')
zebra = Zebra('黑白')
print(elephant)
print(zebra)