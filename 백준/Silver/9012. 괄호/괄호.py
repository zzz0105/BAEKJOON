t = int(input())
for _ in range(t):
    ps = input()
    stack = []
    ans = ''
    for p in ps:
        if p == '(':
            stack.append('(')
        else:
            if stack:
                stack.pop()
            else:
                ans = 'NO'
    print('NO' if ans=='NO' or stack else 'YES')    