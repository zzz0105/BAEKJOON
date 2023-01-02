import sys
input = sys.stdin.readline

N = int(input())
price = [list(map(int,input().split())) for _ in range(N)]
for i in range(N-1):
    price[i+1][0] += min(price[i][1],price[i][2])
    price[i+1][1] += min(price[i][0],price[i][2])
    price[i+1][2] += min(price[i][0],price[i][1])
print(min(price[-1]))