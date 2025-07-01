#Python變數前面帶有"*"時，會自動將你的輸入打包成tuple
def my_sum(*numbers, start = 0):
    ans = 0
    for i in numbers:
        ans+= i
    return start + ans
print(my_sum(1, 2, 3, 4, 5, start = 20))

#內建的sum函式可以帶入第二個參數，起始值，我們的函式也可以