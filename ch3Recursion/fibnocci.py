def fib(x):
    if x == 0:
        return 1
    if x == 1:
        return  1
    else:
        print(f'fib({x-1}) + fib({x-2})')
        return fib(x-1) + fib(x-2)


print(fib(4))


