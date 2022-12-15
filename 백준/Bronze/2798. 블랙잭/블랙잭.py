from itertools import combinations

n, m = map(int,input().split())
nums = map(int,input().split())
combis = combinations(nums, 3)
ans = 0
for combi in combis:
    sum_combi = sum(combi)
    if sum_combi <= m and sum_combi > ans:
        ans = sum_combi
print(ans)