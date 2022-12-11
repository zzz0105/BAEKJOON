def choose(ans):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return 
    else:
        for i in range(len(nums)):
            ans.append(nums[i])
            choose(ans)
            ans.pop()

n, m = map(int,input().split())
nums = sorted(list(set(map(int,input().split()))))
choose([])