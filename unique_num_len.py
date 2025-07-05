# 如何去處理不重複? => Python 中 set 的概念就是鍵不重複
numbers = {1, 2, 3, 1, 2, 3, 4, 1, 2}
print(set(numbers)) # {1, 2, 3, 4} 取出所有不重複的元素

def unique_num_len(numbers):
    return len(set(numbers))


print(unique_num_len(numbers))



