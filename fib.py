# memoization
# python object, keys will be arg to fn, value will return value

def fib(n, memo = {}):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

print(fib(7))
