l, r = input().split()

if len(l)!=len(r):
    print(0)
    
else:
    cnt = 0
    for idx in range(len(l)):
        if l[idx] != r[idx]:
            break
        elif l[idx] == r[idx] == '8':
            cnt += 1
    print(cnt)