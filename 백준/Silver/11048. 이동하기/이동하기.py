N, M = map(int,input().split())
maze = [tuple(map(int,input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        mc = 0
        if i > 0: mc = max(mc,dp[i-1][j])
        if j > 0: mc = max(mc,dp[i][j-1])
        if i > 0 and j > 0: mc = max(mc,dp[i-1][j-1])
        dp[i][j] = maze[i][j] + mc
print(dp[N-1][M-1])