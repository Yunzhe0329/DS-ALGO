# import sys

# mylist = []
# for i in range(15):
#     l_size = sys.getsizeof(mylist)
#     t_size = sys.getsizeof(tuple(mylist))
#     print(f'len = {len(mylist)}, list size = {l_size}, tuple size = {t_size}')
#     mylist.append(i)

# first_last
def first_last(seq):
    return seq[:1] + seq[-1:]

print(first_last('abcde'))
print(first_last([1, 2, 3, 4, 5]))