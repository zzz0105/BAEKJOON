N = int(input())
answer = 1
for n in range(1,N+1):
    answer *= n
    while answer%10==0:
        answer //= 10
    answer %= 10000000000000
    # 곱할 때 0이 최대 8개가 추가되므로, 13자리는 알고 있어야 한다
answer = str(answer%100000)
print('0'*(5-len(answer))+answer)