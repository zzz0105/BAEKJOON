N = int(input())
time = []
price = []
dp = [0]*(N+1)

for _ in range(N):
    t, p = map(int,input().split())
    time.append(t)
    price.append(p)

for i in range(N):
    for j in range(i+time[i], N+1):
        dp[j] = max(dp[i]+price[i], dp[j])

print(dp[N])