n = int(input())
dp = ['']*(n+1)
for x in range(1,n):
    tmp = len(dp[x])+1
    if (len(dp[x+1])>tmp or dp[x+1]==''):
        dp[x+1] = dp[x]+'1'
    if x*2 <= n and (len(dp[x*2])>tmp or dp[x*2]==''):
        dp[x*2] = dp[x]+'2'
    if x*3 <= n and (len(dp[x*3])>tmp or dp[x*3]==''):
        dp[x*3] = dp[x]+'3'
print(len(dp[n]))
for x in dp[n][::-1]:
    print(n, end=' ')
    if x == '1':
        n-=1
    elif x == '2':
        n//=2
    elif x == '3':
        n//=3
print(1)