def choose(ans):
    if len(ans) == m:
        print(*ans)
        return 
    else:
        for i in range(len(nums)):
            ans.append(nums[i])
            choose(ans)
            ans.pop()

n, m = map(int,input().split())
nums = range(1,n+1)
choose([])