def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]

def sum_odd_fibonacci_within_limit(limit):
    sum_odd = 0
    i = 0
    while True:
        fib_num = fibonacci(i)
        if fib_num > limit:
            break
        if fib_num % 2 != 0:
            sum_odd += fib_num
        i += 1
    return sum_odd
result = sum_odd_fibonacci_within_limit(13)
print(result)