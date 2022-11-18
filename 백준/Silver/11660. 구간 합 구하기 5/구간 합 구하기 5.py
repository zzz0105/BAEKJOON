import sys

n, m = map(int,sys.stdin.readline().rstrip().split())
arr = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
acc = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        acc[i][j] = arr[i-1][j-1]+acc[i-1][j]+acc[i][j-1]-acc[i-1][j-1]

res = [tuple(map(int,sys.stdin.readline().rstrip().split())) for _ in range(m)]
for r in res:
    print(acc[r[2]][r[3]]-acc[r[0]-1][r[3]]-acc[r[2]][r[1]-1]+acc[r[0]-1][r[1]-1])