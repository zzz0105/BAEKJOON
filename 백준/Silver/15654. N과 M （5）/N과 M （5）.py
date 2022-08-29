def choose(ans):
    if len(ans) == m:
        print(*ans)
        return 
    else:
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
                choose(ans)
                ans.pop()

n, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
choose([])