from dataclasses import dataclass
@dataclass
class CycleIterator():
    data : list
    max_times : int
    def __post_init__(self):
        self.index = 0
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value
@dataclass   
class CycleList():
    data : list
    max_times : int
    def __iter__(self):
        return CycleIterator(self.data, self.max_times)
        
clist = CycleList(['a', 'b', 'c'], 9)
for c in clist:
    print(c)