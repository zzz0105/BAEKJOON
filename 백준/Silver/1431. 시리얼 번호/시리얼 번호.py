def sum(ns):
    res = 0
    for n in ns:
        if n.isdigit():
            res += int(n)
    return res

S=[input() for _ in ' '*int(input())]
print(*sorted(S,key=lambda x:(len(x),sum(x),x)),sep='\n')