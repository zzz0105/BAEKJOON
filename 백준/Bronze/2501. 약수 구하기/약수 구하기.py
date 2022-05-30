n, k = map(int, input().split())
divisors = []           #n의 약수 리스트

for i in range(1, n+1): #약수 구하기
    if not n % i:       #나누어떨어진다면
        divisors += [i]

if len(divisors) < k:   #n의 약수의 개수가 k개보다 적을 경우 0 출력
    print(0)
else:                   #n의 약수들 중 k번째로 작은 수
    print(divisors[k-1])