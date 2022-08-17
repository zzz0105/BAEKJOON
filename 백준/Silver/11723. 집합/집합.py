import sys
m = int(sys.stdin.readline().rstrip())
s = set()
for _ in range(m):
    i = sys.stdin.readline().rstrip().split()
    if len(i) == 1:
        if i[0]=='all':
            s = set(range(1,21))
        else:
            s.clear()
    else:
        a, b = i
        b = int(b)
        if a == 'add':
            s.add(b)
        elif a == 'remove':
            s.discard(b)    #없는데 remove쓰면 KeyError
        elif a == 'check':
            print(1 if b in s else 0)
        else:
            if b in s:
                s.discard(b)
            else:
                s.add(b)