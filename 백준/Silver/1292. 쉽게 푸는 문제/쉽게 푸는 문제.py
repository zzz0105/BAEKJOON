def total(a):
    ans = 0
    n = 1
    while ((n*(n+1)//2) < a):       #n까지의 개수가 주어진 값보다 작으면
        n += 1
    for i in range(1, n):           #1에서 n까지의 합 구하기
        ans += (i*i)
    ans += ((a - (n*(n-1)//2)) * (n))#나머지 합 더해주기
    return ans

a, b = map(int, input().split())    #구간의 시작과 끝
print(total(b) - total(a-1))        #시작도 포함해야하므로 a-1