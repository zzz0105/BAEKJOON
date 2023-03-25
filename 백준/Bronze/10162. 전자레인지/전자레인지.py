T = int(input())
click = [0,0,0]
time = (300,60,10)
for i in range(3):
    click[i] = T//time[i]
    T %= time[i]
if T:
    print(-1)
else:
    print(*click, sep=' ')