m, t = 1000-int(input()), 0
for c in (500, 100, 50, 10, 5, 1):
    t += m//c
    m %= c
print(t)