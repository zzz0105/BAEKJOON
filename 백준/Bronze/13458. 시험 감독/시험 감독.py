from math import ceil

N = int(input())
A = tuple(map(int, input().split()))
B, C = map(int, input().split())
total = [1] * N
for i in range(N):
    if A[i] <= B:
        continue
    total[i] += ceil((A[i]-B)/C)
    
print(sum(total))