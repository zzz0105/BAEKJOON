import sys

def choose(ans):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return 
    else:
        for i in range(len(nums)):
            ans.append(nums[i])
            choose(ans)
            ans.pop()

n, m = map(int,sys.stdin.readline().rstrip().split())
nums = list(map(int,sys.stdin.readline().rstrip().split()))
nums.sort()
answer = []
choose([])
for a in answer:
    sys.stdout.write(a)
    print()