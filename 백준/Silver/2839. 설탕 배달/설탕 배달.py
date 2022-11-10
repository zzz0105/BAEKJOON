n = int(input())
sugars = [5001] * (max(n+1, 6))
sugars[3] = 1
sugars[5] = 1
for i in range(6, n+1):
    sugars[i] = min(sugars[i], sugars[i-3]+1, sugars[i-5]+1)
print(-1 if sugars[n]==5001 else sugars[n])