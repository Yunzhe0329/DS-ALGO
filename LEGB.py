# liocal variable & Global Variable
x = 0

#def foo():
#    x = 200
#    print(x)
#    print(x)
#foo()
#print(x)

#print('- - - - - - comparason - - - - - -')

# 如果堅持要透過函式改變全域變數 -> global keyword
#def foo_g():
#    global x
#    x = 20
#    print(x)
#print(x)
#foo_g()
#print(x)

#print('- - - - - - comparason - - - - - -')
# 巢狀函式
def foo_nesting(x, y):
    def bar():
        global x
        x = 20
    bar()
    return x * y
print(foo_nesting(10, 10)) #100, suppose to be 200

#  bar() 是使用 global 變數 x -> 而父函式是使用自己的變數
# nonlocal keyword -> Python 會到函式的外層範圍尋找指定的變數，但不包含全域變數
def foo_nesting_nonlocal(x, y):
    def bar():
        nonlocal x
        x = 20
    bar()
    return x * y
print(foo_nesting_nonlocal(10, 10)) #200
