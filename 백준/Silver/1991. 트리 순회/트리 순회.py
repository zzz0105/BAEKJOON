def preorder(v):
    if v != '.':
        print(v, end='')
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):
    if v != '.':
        inorder(tree[v][0])
        print(v, end='')
        inorder(tree[v][1])

def postorder(v):
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end='')

n = int(input())
tree = {}
for _ in range(n):
    p, l, r = input().split()
    tree[p] = [l, r]
preorder('A')
print()
inorder('A')
print()
postorder('A')