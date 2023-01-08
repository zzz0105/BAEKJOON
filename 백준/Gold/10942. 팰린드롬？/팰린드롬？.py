import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int,input().split()))

dp = [[0]*(N) for _ in range(N)]
for length in range(N):
    for i in range(N-length):
        j = i+length
        if i==j:
            dp[i][j] = 1
        elif num[i]==num[j] and (i+1==j or dp[i+1][j-1]==1):
            dp[i][j] = 1

M = int(input())
for _ in range(M):
    S, E = map(int,input().split())
    print(dp[S-1][E-1])