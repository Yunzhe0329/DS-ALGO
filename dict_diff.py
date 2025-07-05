#複習合併 dict
d1 = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 5}
d2 = {'a' : 1, 'b' : 2, 'd' : 4, 'e' : 6}
# key 值相同，右邊的值會覆蓋左邊
merge = d1 | d2
# ** (unpack)解包也能夠做到這件事，可以合併 3 個以上的 dict
merge2 = {**d1, **d2}
print(merge)
print(merge2)

# 要如何知道兩個 Dict 物件的差異?
# 先取得兩個 dict 不重複的鍵
all_keys = set(d1.keys()) | set(d2.keys())
print(all_keys)

def dict_diff(first, second):
    output = {}
    all_keys = sorted(first.keys()|second.keys())
    
    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]
    return output
print(dict_diff(d1, d2))
