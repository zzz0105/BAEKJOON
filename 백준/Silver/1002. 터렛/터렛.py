T = int(input())
for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    d = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**0.5
    if d == 0:
        print(-1 if r1==r2 else 0)
    else:
        rp, rm = r1+r2, abs(r1-r2)
        print(1 if d==rp or d==rm else (2 if rm<d<rp else 0))