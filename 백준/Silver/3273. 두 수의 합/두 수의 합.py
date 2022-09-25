n = int(input())
nums = list(map(int,input().split()))
nums.sort()
x = int(input())
cnt = 0
l, r = 0, n-1
while l<r:
    tmp = nums[l] + nums[r]
    if tmp == x:
        cnt += 1
        l += 1
    elif tmp < x:
        l += 1
    else:
        r -= 1
print(cnt)