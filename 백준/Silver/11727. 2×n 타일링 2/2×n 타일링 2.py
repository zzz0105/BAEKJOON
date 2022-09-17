n = int(input())
sq = [0, 1, 3] + [0] * (n-2)
for i in range(3, n+1):
    sq[i] = sq[i-2]*2 + sq[i-1]
print(sq[n]%10007)