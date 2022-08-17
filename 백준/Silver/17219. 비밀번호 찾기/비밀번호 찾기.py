n, m = map(int,input().split())
pw_dic = {}
pws = []
for _ in range(n):
    ad, pw  = input().split()
    pw_dic[ad] = pw
for _ in range(m):
    pws.append(pw_dic[input()])
print(*pws, sep='\n')