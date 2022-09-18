n = int(input())
nums = list(map(int,input().split()))
tot = [nums[0]] + [0] * (n-1)
for i in range(n):
    tot[i] = max(tot[i-1]+nums[i], nums[i])
print(max(tot))