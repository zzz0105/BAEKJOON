N = int(input())
A = sorted(map(int,input().split()),reverse=True)
B = sorted(map(int,input().split()))
print(sum(map(lambda x,y:x*y, A,B)))