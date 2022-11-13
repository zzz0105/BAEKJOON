def pr(a,b):
    global c
    if b == 1:
        return a%c
    tmp = pr(a,b//2)
    return tmp*tmp*a%c if b%2 else tmp*tmp%c 

a,b,c = map(int,input().split())
print(pr(a,b))