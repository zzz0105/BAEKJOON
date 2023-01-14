import sys

def check(now):
    if len(now)==len(S):
        if now==S:
            print(1)
            sys.exit()
        return
    if now[-1]=='A':
        now.pop()
        check(now)
        now.append('A')
    if now[0]=='B':
        now.reverse()
        now.pop()
        check(now)
        now.append('B')
        now.reverse()

S = list(input())
T = list(input())
check(T)
print(0)