from itertools import combinations
n, s = map(int, input().split())
nums = list(map(int, input().split()))
combis = []
cnt = 0
for r in range(1, len(nums)+1):
    combis.append(list(combinations(nums, r)))
for combi in combis:
    for c in combi:
        if sum(c)==s:
            cnt += 1
print(cnt)