def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def isPalin(n):
    n = str(n)
    if n == n[::-1]:
        return True
    return False

N = int(input())
while True:
    if isPrime(N) and isPalin(N):
        print(N)
        break
    N += 1