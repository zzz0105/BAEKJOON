import sys
n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]
for a in sorted(arr):
    print(a)