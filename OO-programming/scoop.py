class Scoop:
    def __init__(self, flavor):
        self.flavor = flavor
    def __repr__(self):
        return f'Scoop({self.flavor})'

class Scoop_Maker:
    def create(self, flavors):
        return [Scoop(flavor) for flavor in flavors]
class Bowl:
    max_scoops = 3
    def __init__(self):
        self.scoops = []
    def add_scoop(self, *new_scoops):
        for new_scoop in new_scoops:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(new_scoop)
    # __str__() 通常用來回傳「非正式」字串，給使用者參考
    #def __str__(self):
    #    flavors = ', '.join(scoop.flavor for scoop in self.scoops)    
    #    return f'冰淇淋碗口味 : {flavors}'
    #__repr__()通常用來回傳「正式」字串，for 除錯使用
    def __repr__(self):
        return f'Bowl(scoops = {self.scoops})'   
class ExtraBowl(Bowl):
    max_scoops = 5
scoop_maker = Scoop_Maker()
scoops = scoop_maker.create(['巧克力', '草莓', '花生'])

bowl = Bowl()
bowl.add_scoop(Scoop('香草'), Scoop('百香果'), Scoop('覆盆莓'), Scoop('芋頭'))

extrabowl = ExtraBowl()
extrabowl.add_scoop(Scoop('香草'), Scoop('百香果'), Scoop('覆盆莓'), Scoop('芋頭'))
print(bowl)
print("-------------comparason------------")
print(extrabowl)
for scoop in scoops:
    print(scoop, scoop.flavor)