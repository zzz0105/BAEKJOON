n = int(input())
money = sorted(map(int, input().split()))
tot = int(input())
if sum(money)<=tot:
    print(max(money))
else:
    l, r = 0, max(money)
    while l<=r:
        tmp = 0
        m = (l+r)//2
        for mon in money:
            tmp += min(mon, m)
        if tmp > tot:
            r = m - 1
        else:
            l = m + 1
    print(r)