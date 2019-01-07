
def solution(n):
    if n == 0:
        return 1
    else:
        return n * solution(n-1)

print(solution(12))