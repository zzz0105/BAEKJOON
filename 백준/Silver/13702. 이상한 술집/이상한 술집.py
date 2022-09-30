n, k = map(int,input().split())
kettles = [int(input()) for _ in range(n)]
l, r = 1, max(kettles)
while l <= r:
    m = (l+r)//2
    tmp = sum(map(lambda x: x//m, kettles))
    if tmp >= k:
        res = m
        l = m + 1
    else:
        r = m - 1
print(res)