# 閉包函式
def add(n):
    def closure(x):
        return n+x
    return closure # 回傳子函式
my_add = add(10)
print(my_add(5))
print(my_add(7))


import random

def set_passwd_source(source):
    def passwd_gen(length):
        output = []
        for i in range (length):
            output.append(random.choice(source))
        return ''.join(output)
    return passwd_gen
my_password_gen = set_passwd_source('0123456789abcdefghijk') #你密碼內容的選取範圍
print(my_password_gen(8)) #生成的密碼長度
