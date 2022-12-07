from collections import Counter

def choose(ans):
    if len(ans) == m:
        ans = ' '.join(map(str,ans))
        if ans not in answer:
            answer.append(ans)
        return 
    else:
        j = 0 if len(ans)==0 else nums.index(ans[-1])
        for i in range(j,len(nums)):
            if nums_cnt[nums[i]]>ans.count(nums[i]) :
                ans.append(nums[i])
                choose(ans)
                ans.pop()

n, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
nums_cnt = Counter(nums)
answer = []
choose([])
print(*answer, sep='\n')