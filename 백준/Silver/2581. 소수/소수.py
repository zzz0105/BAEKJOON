m = int(input())
n = int(input())
primes = []     #소수 리스트
tot_primes = 0  #소수 총합
for num in range(m, n+1):
    for i in range(2, num+1):
        if num == i:  #소수면 리스트에 추가하고 소수 총합에 더하기
            primes.append(num)
            tot_primes += num
        if num%i == 0:
            break
if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(primes[0])