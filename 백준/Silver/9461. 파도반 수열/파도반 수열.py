t = int(input())
nums = [int(input()) for _ in range(t)]
m = max(nums)
result = [0, 1, 1, 1, 2]
for i in range(5, m+1):
    result.append(result[i-1] + result[i-5])
for j in nums:
    print(result[j])