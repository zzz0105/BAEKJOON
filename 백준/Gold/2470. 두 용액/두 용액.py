N = int(input())
sol = sorted(map(int,input().split()))
answer = ()
diff = 2000000001
l, r = 0, N-1

while l < r < N:
    mixed = sol[l] + sol[r]
    if abs(mixed) < diff:
        diff = abs(mixed)
        answer = (sol[l], sol[r])
        if mixed == 0:
            break
    if mixed > 0:
        r -= 1
    else:
        l += 1

print(*answer,sep=" ")