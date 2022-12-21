def isPrime(n):
    if n==1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True if D in str(n) else False

A, B, D = map(int,input().split())
D = str(D)
answer = 0
for n in range(A, B+1):
    if isPrime(n):
        answer += 1
print(answer)