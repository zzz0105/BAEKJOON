def sol(n, row, col):
    global ans
    if n == 1:
        ans += 2*row + col
        return
    now = 2**(n-1)
    ans += 4**(n-1) * (2*(row//now)+(col//now))
    sol(n-1, row%now, col%now)

N, r, c = map(int, input().split())
ans = 0
sol(N, r, c)
print(ans)