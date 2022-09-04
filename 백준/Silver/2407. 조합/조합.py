def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

n, m = map(int,input().split())
print(fact(n) // (fact(m) * fact(n-m)))