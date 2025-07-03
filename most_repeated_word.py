# 撰寫一個函式，傳入一個單字，回傳該單字中重複最多的字母
import operator
def most_repeated_letter(word):
    # set 的特性是元素唯一，這裡用來取得單字中不重複的字母
    letters = list(set(word))
    letters_count = []
    for letter in letters:
        #append() 只能接受一個參數，這裡傳入的是 (letter, count) 的 tuple 用 tuple 封裝兩個值後再加入列表
        letters_count.append((letter, word.count(letter)))
    #預設是遞增排序
    result = sorted(letters_count, key = operator.itemgetter(1))[-1] 
    print(result)

most_repeated_letter("independence")

# 用 Python 內建的 Counter 容器
from collections import Counter
def most_repeated_letter_counter(word):
    result = Counter(word).most_common(1)[0]
    print(f'{result[0]} 重複了 {result[1]} 次')

most_repeated_letter_counter("independence")

print(Counter("independence" ))
#Counter({'e': 4, 'n': 3, 'd': 2, 'i': 1, 'p': 1, 'c': 1})