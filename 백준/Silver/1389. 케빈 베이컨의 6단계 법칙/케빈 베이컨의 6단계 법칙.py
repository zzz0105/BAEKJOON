n, m = map(int,input().split())
friends = [[float('inf')]*n for _ in range(n)]

for _ in range(m):
    a, b = map(int,input().split())
    friends[a-1][b-1] = 1
    friends[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                friends[i][j] = 0
            else:
                friends[i][j] = min(friends[i][j], friends[i][k]+friends[k][j])

b = float('inf')
for idx in range(n):
    tmp = sum(friends[idx])
    if b > tmp:
        b = tmp
        ans = idx

print(ans + 1)