import sys
n = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(n):
    c = sys.stdin.readline().rstrip().split()
    if c[0] == 'push':
        stack.append(c[1])
    elif c[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)