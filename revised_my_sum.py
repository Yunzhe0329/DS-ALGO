def my_sum(*items):
    if not items:
        return items
    ans = items[0]
    for item in items[1:]:
        if isinstance(item, dict):
            ans|= item 
        else:
            ans += item
    return ans

print(my_sum())
print(my_sum(10, 20, 30, 40))
print(my_sum('abc','d', 'e'))
print(my_sum([10, 20, 30],[40, 50], [60]))
print(my_sum({'A' : 1, 'B' : 2},{'C' : 3} ))

# dict 物件的加總與合併,dict 是 key, value的形式，不適用上面定義的函式
# d1 = {'A' : 1, 'B' : 2}
# d2 = {'C' : 3}
# print({**d1, **d2}) # 用**解包d1和d2的元素，再產生新的dict物件，不會影響d1和d2

# #將d2和d1合併，會直接改變物件內容
# d1.update(d2)
# print(d1)

# #Python3.9 可以直接使用Union的運算符處理 dict上述情況
