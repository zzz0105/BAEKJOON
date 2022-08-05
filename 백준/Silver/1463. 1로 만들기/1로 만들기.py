n = int(input())
nums = [0] * (n+1)
for i in range(1, n):
  if (nums[i+1]>nums[i]+1 or nums[i+1]==0):
    nums[i+1] = nums[i]+1
  if i*2 <= n and (nums[i*2]>nums[i]+1 or nums[i*2]==0):
    nums[i*2] = nums[i]+1
  if i*3 <= n and (nums[i*3]>nums[i]+1 or nums[i*3]==0):
    nums[i*3] = nums[i]+1
print(nums[n])