n, m = map(int,input().split())
packs = []
ones = []
for _ in range(m):
    pack, one = map(int,input().split())
    packs.append(pack)
    ones.append(one)
min_packs = min(packs)
min_ones = min(ones)
price = 0
while True:
    if n >= 6:
        price += min(min_ones*6, min_packs) * (n//6)
        n %= 6
    else:
        price += min(min_ones*n, min_packs)
        break
print(price)