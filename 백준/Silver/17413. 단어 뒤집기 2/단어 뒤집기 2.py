def print_stack():
    while stack:
        print(stack.pop(), end='')

S = input()
stack = []
in_bracket = False
for s in S:
    if s=='<':
        in_bracket = True
        print_stack()
    elif s=='>':
        in_bracket = False
        print('>', end='')
        continue
    
    if in_bracket:
        print(s, end='')
    else:
        if s==' ':
            print_stack()
            print(' ', end='')
        else:
            stack.append(s)
print_stack()