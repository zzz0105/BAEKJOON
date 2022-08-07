tc = int(input())
ns = []
for _ in range(tc):
    ns.append(int(input()))
n = max(ns)

nums = [0,1,1,1] + [0]*(n-3)
for i in range(2, n+1):
    if i==2:
        nums[i] += nums[i-2] + nums[i-1]
    else:
        nums[i] += nums[i-3] + nums[i-2] + nums[i-1]  

for nn in ns:
    print(nums[nn])