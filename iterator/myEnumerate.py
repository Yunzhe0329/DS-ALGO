# 此範例同時是 iterable & Iterator
class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self  # 回傳物件本身當作走訪器
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = (self.index, self.data[self.index]) #用 tuple 回傳（索引, 值）
        self.index += 1
        return value
myEnum = MyEnumerate('abcde')
for index, letter in myEnum:
    print(f'{index} -> {letter}')
#iterable 物件 VS Iterator 物件
# Python 的每種容器（list、dict、str...）在呼叫 iter() 時，都會額外產生一個不同的專屬 iterator 類別
n = [1, 2, 3, 4, 5]
print(type(iter(n)))

d = {'a' : 1, 'b' : 2, 'c' : 3}
print(type(iter(d)))

s = 'test'
print(type(iter(s)))