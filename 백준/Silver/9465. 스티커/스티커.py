T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        sticker.append(tuple(map(int,input().split())))
    dp = [[0]*n for _ in range(2)]
    for j in range(2):
        dp[j][0] = sticker[j][0]
    if n > 1:
        for j in range(2):
            dp[j][1] = dp[j-1][0] + sticker[j][1]
        for i in range(2,n):
            for j in range(2):
                dp[j][i] = max(dp[j-1][i-1], dp[j-1][i-2]) + sticker[j][i]
    print(max(dp[0][-1], dp[1][-1]))