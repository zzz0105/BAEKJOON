def choose(ans, s):
    if len(ans) == 6:
        print(' '.join(map(str, ans)))
        return 
    else:
        i = 0 if len(ans)==0 else s.index(ans[-1])
        for idx in range(i,len(s)):
            if s[idx] not in ans:
                ans.append(s[idx])
                choose(ans, s)
                ans.pop()

while True:
    k, *s = map(int,input().split())
    s.sort()
    if k == 0:
        break
    choose([], s)
    print()