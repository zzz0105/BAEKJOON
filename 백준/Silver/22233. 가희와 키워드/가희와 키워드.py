import sys
n, m  = map(int,sys.stdin.readline().rstrip().split())
memo = set(sys.stdin.readline().rstrip() for _ in range(n))
for _ in range(m):
    memo -= set(sys.stdin.readline().rstrip().split(','))
    print(len(memo))