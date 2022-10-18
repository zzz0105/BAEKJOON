n = int(input())
max_ord = 97

premises = [['F']*26 for _ in range(26)]
for _ in range(n):
    tmp = input().split()
    premises.append((ord(tmp[0]),(tmp[-1])))
    premises[ord(tmp[0])-97][ord(tmp[-1])-97] = 'T'
    max_ord = max(max_ord, ord(tmp[0]), ord(tmp[-1]))

max_ord -= 96
for k in range(max_ord):
    for a in range(max_ord):
        for b in range(max_ord):
            if premises[a][k]=='T' and premises[k][b]=='T':
                premises[a][b] = 'T'

m = int(input())
for _ in range(m):
    tmp = input().split()
    print(premises[ord(tmp[0])-97][ord(tmp[-1])-97])