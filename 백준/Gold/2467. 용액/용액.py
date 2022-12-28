N = int(input())
solutions = tuple(map(int,input().split()))
answer = ''
l, r = 0, N-1
min_s = float('inf')
while l < r:
    tmp = solutions[l]+solutions[r]
    if abs(tmp) < min_s:
        answer = (solutions[l], solutions[r])
        min_s = abs(tmp)
    if tmp > 0:
        r -= 1
    elif tmp < 0:
        l += 1
    else:
        break
print(*answer, sep=' ')