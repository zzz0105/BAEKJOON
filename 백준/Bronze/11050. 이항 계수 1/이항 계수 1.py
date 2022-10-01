def fact(m):
    if m > 1:
        return m * fact(m-1)
    else:
        return 1

n, k = map(int,input().split())
print(fact(n)//fact(k)//fact(n-k))