people =[
    ('Joe', 'Biden', 'president@usa.gov'),
    ('Emmanuel', 'Macron', 'president@france.gov'),
    ('Justin', 'Trudeau', 'president@canada.gov'),
    ('Angela', 'Merkel', 'president@germany.gov'),
    ('Jacinda', 'Andern', 'president@newzealand.gov')
]

#直觀的做法, 直接使用sorted()
#問題點 : sorted()會按照tuple中元素的順序排序，在此case中會依序用名字、姓氏、電郵來排序（邏輯有問題）
# for person in sorted(people):
#     print(person)

#要依照姓氏做排序   
def last_to_first_sorting(data):
    return (data[1], data[0])
# 使用 sorted() 函數對 people 清單排序
# 並指定 key=last_to_first_sorting，表示排序時會對每個人用這個函數產生排序依據
for person in sorted(people, key = last_to_first_sorting):
    print(person)

print("------Comparason------")
# lambda expression
# 使用 sorted() 對 people 清單進行排序
# key 是一個匿名函數（lambda expression），用來告訴 sorted 如何排序
# lambda data: (data[1], data[0]) 的意思是：
# 對每個元素（如 ("John", "Smith")）取出 (姓氏, 名字) 作為排序依據
# 所以會先依照姓氏排序，如果姓氏相同，才依照名字排序
for person in sorted(people, key = lambda data : (data[1], data[0])):
    print(person)

print("------Comparason------")
# lambda 表達式可讀性較低，這裡使用 Python 的 operator 模組來提高可讀性
# operator.itemgetter(1, 0) 表示要根據元素的索引 1和索引 0來排序
# 適用於 list 中的每個元素本身也是一個序列（例如 tuple）
import operator
for person in sorted(people, key = operator.itemgetter(1, 0)):
    print(person)
