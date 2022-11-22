import sys
from collections import Counter
n = int(sys.stdin.readline().rstrip())
nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
nums.sort()
print(round(sum(nums)/n))
print(nums[n//2])
nums_cnt = Counter(nums).most_common(2)
print(nums_cnt[1][0] if len(nums)>1 and nums_cnt[0][1]==nums_cnt[1][1] else nums_cnt[0][0])
print(max(nums)-min(nums))