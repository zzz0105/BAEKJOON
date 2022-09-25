k, n = map(int,input().split())
wires = [int(input()) for _ in range(k)]
l, r = 1, max(wires)
while l <= r:
    m = (l + r) // 2
    tmp = sum(map(lambda x:x//m, wires))
    if n <= tmp:
        l = m + 1
    else:
        r = m - 1
print(r)