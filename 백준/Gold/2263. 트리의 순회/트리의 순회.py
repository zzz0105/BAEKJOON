import sys
sys.setrecursionlimit(10**8)

def preorder(in_start, in_end, post_start, post_end):
    if in_start>in_end or post_start>post_end:
        return

    parent = postorder[post_end]
    print(parent, end = ' ')

    left = pos[parent] - in_start   #왼쪽 인자 개수
    right = in_end - pos[parent]    #오른쪽 인자 개수
    preorder(in_start, in_start + left - 1, post_start, post_start + left - 1)
    preorder(in_end-right + 1, in_end, post_end - right, post_end - 1)

n = int(input())    #정점 개수
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0]*(n+1)
for i in range(n):
    pos[inorder[i]] = i

preorder(0, n-1, 0, n-1)