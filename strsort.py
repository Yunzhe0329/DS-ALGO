# sort() VS sorted()
# String 無法使用sort()進行排序
# s = 'python'
# print(s.sort())
# l = list(s)
# print(l) #['p', 'y', 't', 'h', 'o', 'n']

#sorted()可以直接做到這件事
def strsort(word):
    return ''.join(sorted(word, key=str.lower)) #處理大小寫的情況，如此才不會產生錯誤

print(strsort("python"))