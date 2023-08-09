def isPrime(num):
    for d in range(2,int(num**0.5)+1):
        if num%d == 0:
            return False
    return True

def solution(n):
    answer = 0
    for num in range(2,n+1):
        answer += 1 if isPrime(num) else 0
    return answer