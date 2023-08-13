from collections import defaultdict

N, K = map(int,input().split())
nums = tuple(map(int,input().split()))
max_len = 0
l, r = 0, 0
count = defaultdict(int)

while l <= r and r < N:
    if count[nums[r]] < K:
        count[nums[r]] += 1
        r += 1
        max_len = max(max_len, r-l)
    else:
        count[nums[l]] -= 1
        l += 1
        
print(max_len)