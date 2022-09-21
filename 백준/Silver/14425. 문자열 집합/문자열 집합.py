n, m = map(int,input().split())
sn = set(input() for _ in range(n))
ans = 0
for _ in range(m):
    if input() in sn:
        ans += 1
print(ans)