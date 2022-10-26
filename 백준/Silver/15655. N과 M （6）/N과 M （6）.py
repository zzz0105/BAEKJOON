def choose(ans):
    if len(ans) == m:
        print(*ans)
        return 
    else:
        j = 0 if not ans else nums.index(ans[-1])+1
        for i in range(j,len(nums)):
            ans.append(nums[i])
            choose(ans)
            ans.pop()

n, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
choose([])