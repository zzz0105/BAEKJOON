import sys
n, m = map(int,sys.stdin.readline().rstrip().split())
name_to_group = {}
group_to_name = {}
for _ in range(n):
    group = sys.stdin.readline().rstrip()
    p = int(sys.stdin.readline().rstrip())
    for _ in range(p):
        name = sys.stdin.readline().rstrip()
        name_to_group[name] = group
        group_to_name[group] = group_to_name.get(group,[]) + [name]
for _ in range(m):
    quiz = sys.stdin.readline().rstrip()
    q = sys.stdin.readline().rstrip()
    if q=='1':
        print(name_to_group[quiz])
    else:
        print(*sorted(group_to_name[quiz]),sep='\n')