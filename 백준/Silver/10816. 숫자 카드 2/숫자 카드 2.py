from collections import Counter

n = int(input())
nums = Counter(map(int,input().split()))
m = int(input())
sang = map(int,input().split())
for s in sang:
    print(nums[s], end=' ')