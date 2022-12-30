import sys
sys.setrecursionlimit(10**6)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

N = int(input())
answer = 0
for s in str(factorial(N))[::-1]:
    if s=='0': answer += 1
    else: break
print(answer)