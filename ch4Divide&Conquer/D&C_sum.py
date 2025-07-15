def DC_sum(list):
    if list == []:
        return 0
    else:
        return list[0] + DC_sum(list[1:])

print(DC_sum([2, 4, 6]))

def counter(list):
    if list == []:
        return 0
    return 1 + counter(list[1:])

def find_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = find_max(list[1:])
    return list[0] if list[0] > sub_max else sub_max
print(find_max([1, 3, 5]))
