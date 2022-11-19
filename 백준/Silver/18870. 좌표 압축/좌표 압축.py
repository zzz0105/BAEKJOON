import sys
n = int(sys.stdin.readline().rstrip())
nums = tuple(map(int, sys.stdin.readline().rstrip().split()))
sn = sorted(tuple(set(nums)))
dic = {}
for idx in range(len(sn)):
    dic[sn[idx]] = idx
for i in nums:
    print(dic[i], end=' ')