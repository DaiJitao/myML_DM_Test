def fib_ssis(n, memo):
    if memo[n] != -1:
        return memo[n]
    elif n <= 2:
        memo[n] = 1
    else:
        memo[n] = fib_ssis(n-1, memo) + fib_ssis(n-2, memo)
    return memo[n]



def fib(n):
    if n <= 0:
        return 0
    memo = [-1] * (n + 1)
    return fib_ssis(n, memo)


def fib2(n):
    if n <= 0:
        return 0
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 1
    for i in range(3, n+1):
        memo[i] = memo[i - 1] + memo[i-2]
    return memo[n]


print (fib(100))
print(fib(100))