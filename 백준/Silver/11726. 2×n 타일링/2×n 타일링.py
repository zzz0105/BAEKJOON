n = int(input())
width = [0] * (n+1)
width[1] = 1
if n > 1:
    width[2] = 2
    for i in range(3,n+1):
        width[i] = width[i-1] + width[i-2]
print(width[n]%10007)