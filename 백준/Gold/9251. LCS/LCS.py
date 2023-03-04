A = input()
B = input()
la1, lb1 = len(A)+1, len(B)+1
dp = [[0]*(lb1) for _ in range(la1)]
for i in range(1,la1):
    for j in range(1,lb1):
        if A[i-1]==B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])