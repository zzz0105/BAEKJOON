from itertools import permutations

n = int(input())
nums = map(int,input().split())
ans = float('-inf')
permus = permutations(nums, n)
for permu in permus:
    tmp = 0
    for idx in range(n-1):
        tmp += abs(permu[idx] - permu[idx+1])
    ans = max(ans, tmp)  
      
print(ans)