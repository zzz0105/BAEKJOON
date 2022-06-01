n = int(input())
nums = list(map(int, input().split()))  #n개의 수
prime = 0   #소수 개수
for num in nums:
    for x in range(2, num+1):
        if x==num:
            prime += 1
        if num%x==0:    #나누어떨어지면 소수아님
            break
print(prime)