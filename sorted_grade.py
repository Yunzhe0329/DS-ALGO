#用排版格式輸出容器內容
grades = [
    ('Alice', 'Woody', 89),
    ('Bob', 'Johnson', 86),
    ('Cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91)
]
#寫出一個函式 sorted_grades()會將資料照成績排序後，以字串格式加入適當的間隔與換行，並return 字串

import operator
def sorted_grades(grade):
    grade.sort(key = operator.itemgetter(2), reverse=True) #依據 index = 2, 進行遞減排序
    output = []
    for first, last, grade in grades:
        output.append(f'{last:12s}{first:10s}{grade:.1f}') # f-string做格式化輸出，s是字串的縮寫，代表要空出幾個字元
    return '\n'.join(output)
print("使用f-string處理的結果\n")
print(sorted_grades(grades),'\n')

print("----------Comparason----------","\n")
# Python 內建的 format() 去處理
def sorted_grades_with_format(grade):
    grade.sort(key = operator.itemgetter(2), reverse = True)
    output = []
    for first, last, grade in grades:
        output.append('{:<12s}{:<8s}{:.1f}'.format(last, first, grade))
    return '\n'.join(output)
print("使用format處理的結果\n")
print(sorted_grades_with_format(grades))



# 使用f-string處理的結果

# Letterman   Cindy     93.0
# Williams    Eddie     91.0
# Woody       Alice     89.0
# Johnson     Bob       86.0
# Moor        David     86.0 

# ----------Comparason---------- 

# 使用format處理的結果

# Letterman   Cindy   93.0
# Williams    Eddie   91.0
# Woody       Alice   89.0
# Johnson     Bob     86.0
# Moor        David   86.0