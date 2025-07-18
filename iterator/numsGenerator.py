def numsGenerator(num):
        return (int(digit) for digit in str(num) if digit.isnumeric())

numbers = numsGenerator(3.14159)

for num in numbers:
        print(num)