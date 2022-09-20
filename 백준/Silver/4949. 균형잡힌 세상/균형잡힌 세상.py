ans = []
while True:
    word = input()
    stack = []
    if word == '.':
        break
    for s in word:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                ans.append('no')
                break
        elif s == ']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                ans.append('no')
                break
        if s == '.':
            if not stack:
                ans.append('yes')
            else:
                ans.append('no')
        
print(*ans, sep='\n')