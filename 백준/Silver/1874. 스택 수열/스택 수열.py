n = int(input())
nums = []
ans = []
now = 1
tmp = 0

for i in range(n):
    num = int(input())
    while now <= num:
        nums.append(now)
        ans.append('+')
        now += 1
    if nums[-1] == num:
        nums.pop()
        ans.append('-')
    else:
        tmp = 1
if tmp == 0:
    print(*ans, sep="\n")
else:
    print("NO")
