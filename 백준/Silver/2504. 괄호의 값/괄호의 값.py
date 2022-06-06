brackets = list(input())
s = []  #스택
ans = 0
tmp = 1
#여는 괄호일 때 tmp에 값을 곱해나간다
#닫는 괄호일 때 tmp를 ans에 더해주고 tmp를 초기화한다
for i in range(len(brackets)):
    if brackets[i] == '(':
        s.append(brackets[i])
        tmp *= 2
    elif brackets[i] == '[':
        s.append(brackets[i])
        tmp *= 3

    elif brackets[i] == ')':
        if not s or s[-1]=='[':
            ans = 0
            break
        if brackets[i-1]=="(":
            ans += tmp
        s.pop()
        tmp//=2
    elif brackets[i] == ']':
        if not s or s[-1]=='(':
            ans = 0
            break
        if brackets[i-1]=="[":
            ans += tmp
        s.pop()
        tmp//=3

print(0 if s else ans)