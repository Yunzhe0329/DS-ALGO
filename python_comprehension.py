# list comprehension
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(nums)
print(squares)
# sum of even squares:
even_square_sum = sum([x** 2 for x in nums if x % 2 == 0])
print('偶數的平方和 ：', even_square_sum)
# abs_numbers()
#nums_1 = [1, -2, 3, -4, 5]
def abs_list(your_list):
    abs_number = [abs(x) for x in your_list]
    print('原始容器 : ', your_list)
    print('不更改原本資料變成絕對值：', abs_number)
abs_list([-3, -2, 6, -10, 9])

#內建 map() 也有comprehension 的味道
def abs_list(numbers):
    return list(map(abs, numbers))
print(abs_list([1, -2, 3, -4, -5]))
