n = int(input())
m = n
cnt = 0
while True:
    cnt += 1
    tmp = m%10*10+(m//10+m%10)%10
    if tmp==n:
        print(cnt)
        break
    else:
        m = tmp