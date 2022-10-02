import sys
n, k = map(int,sys.stdin.readline().rstrip().split())
nums = sorted(map(int,sys.stdin.readline().rstrip().split()))
print(nums[k-1])