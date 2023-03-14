t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, kind = input().split()
        clothes[kind] = clothes.get(kind,[])+[name]
        
    answer = 1
    for key in clothes:
        answer *= len(clothes[key])+1
    print(answer-1)