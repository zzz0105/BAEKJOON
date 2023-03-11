N = int(input())
ropes = sorted(list(int(input()) for _ in range(N)))
max_weight = ropes[-1]
for i in range(N):
    max_weight = max(max_weight, ropes[i]*(N-i))
print(max_weight)