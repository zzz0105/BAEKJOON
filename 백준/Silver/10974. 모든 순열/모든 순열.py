from itertools import permutations
n = int(input())
res = tuple(permutations(range(1,n+1), n))
for i in range(len(res)):
    print(*res[i], sep=' ')