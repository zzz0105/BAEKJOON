n = int(input())
ns = set(map(int,input().split()))
m = int(input())
ms = map(int,input().split())
for mm in ms:
    print(1 if mm in ns else 0)