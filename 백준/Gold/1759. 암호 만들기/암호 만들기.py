def back(ans):
    global answer
    if len(ans)==l:
        if len(set(ans)&v)>=1 and len(set(ans)&c)>=2:
            answer.append(''.join(ans))
        return
    j = 0 if len(ans)==0 else alpha.index(ans[-1])
    for i in range(j, len(alpha)):
        if alpha[i] not in ans:
            ans.append(alpha[i])
            back(ans)
            ans.pop()

l, c = map(int, input().split())
alpha = input().split()
alpha.sort()
vowel = {'a','i','e','o','u'}
v = set(alpha) & vowel
c = set(alpha) - v
answer = []
back([])
print(*answer, sep='\n')