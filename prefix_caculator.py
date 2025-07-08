def prefix(to_solve):
    op, num1, num2 = to_solve.split()
    print(num1, op, num2)
prefix('+ 2 3')

import operator
def prefix_cal(to_solve):
    operation = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv
    }
    op, num1, num2 = to_solve.split()
    return operation[op](float(num1), float(num2))
print(prefix_cal('+ 2 3'))

# complete prefix caculator
def prefix_caculator(to_solve):
    operation = {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.truediv
    }
    def isNumber(num):
        return num.replace('.', '').isnumeric()

    items = to_solve.split()
    while len(items) > 1:
        for i in range(len(items)-2):
            op, n1, n2 = items[i:i+3]
            if op in operation and isNumber(n1) and isNumber(n2):
                break
        items = items[:i] +[str(operation[op](float(n1), float(n2)))] + items[i+3:]
    return float(items[0])
print(prefix_caculator('/ * + 2 4 3 + 1 5'))
