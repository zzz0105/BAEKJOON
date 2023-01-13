import sys
input = sys.stdin.readline

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if not n%i:
            return False
    return True

N = int(input())

primes = []
for n in range(2,N+1):
    if is_prime(n):
        primes.append(n)

prefix_sum = [0]
for prime in primes:
    prefix_sum.append(prefix_sum[-1]+prime)

l, r, answer = 0, 1, 0
L_ps = len(prefix_sum)
while l!=L_ps-1:
    now = prefix_sum[r] - prefix_sum[l]
    if now == N:
        answer += 1
    if now <= N:
        if r == L_ps-1:
            l += 1
        else:
            r += 1
    else:
        l += 1

print(answer)