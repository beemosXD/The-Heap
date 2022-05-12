# memoization
# python object, keys will be arg to fn, value will return value

def fib(n, memo = {}): # memo stores n as key values our return values for function
    if (n in memo): return memo[n];
    if (n <= 2): return 1;
    memo[n] = fib(n-1, memo) + fib(n-2, memo); # stores result as memo
    return memo[n];

print(fib(50))
  