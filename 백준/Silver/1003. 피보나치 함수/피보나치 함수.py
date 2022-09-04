import sys

t = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(t)]
mn = max(nums)
fib = [[0, 0] for _ in range(mn+1)]
fib[0] = [1, 0]
if mn > 0:
    fib[1] = [0, 1]
for i in range(2, mn+1):
    fib[i][0] = fib[i-1][0] + fib[i-2][0]
    fib[i][1] = fib[i-1][1] + fib[i-2][1]
for j in range(t):
    print(*fib[nums[j]])