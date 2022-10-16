n = int(input())
is_friend = [list(input()) for _ in range(n)]
fg = [[0]*n for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a==b:
                continue
            if is_friend[a][b]=='Y' or (is_friend[a][k] == 'Y' and is_friend[k][b] =='Y'):
                fg[a][b] = 1

ans = 0
for f in fg:
    ans = max(ans, sum(f))
print(ans)