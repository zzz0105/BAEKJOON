n, m = map(int,input().split())
nums = tuple(map(int,input().split()))
num_sum = [0] * (n+1)
for i in range(n):
    num_sum[i+1] = num_sum[i] + nums[i]
idxs = [tuple(map(int,input().split())) for _ in range(m)]
for idx in idxs:
    print(num_sum[idx[1]]-num_sum[idx[0]-1])