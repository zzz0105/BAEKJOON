from collections import deque
import sys
input = sys.stdin.readline

def D(n): return 2*n % 10000
def S(n): return (n-1) % 10000
def L(n): return n//1000 + (n%1000)*10
def R(n): return (n%10)*1000 + n//10

T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    
    q = deque([(A, '')])
    visited = [False]*(10001)
    while q:
        n, ops = q.popleft()
        if n == B:
            print(ops)
            break
        for nop, res in (('D',D(n)),('S',S(n)),('L',L(n)),('R',R(n))):
            if not visited[res]:
                visited[res] = True
                q.append((res, ops+nop))