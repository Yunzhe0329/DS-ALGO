# 壓縮二維陣列

# 一般來說
my_list = []
for x in [[1, 2], [3, 4]]:
    for y in x:
        my_list.append(y)
print(my_list)

# with comprehension
def flatten(data):
    return [sub_element
            for element in data
                for sub_element in element]
print(flatten([[1, 2], [3, 4]]))
