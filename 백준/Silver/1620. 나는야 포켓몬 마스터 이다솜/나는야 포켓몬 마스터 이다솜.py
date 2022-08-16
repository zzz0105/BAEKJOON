n, m = map(int,input().split())
pokemon_num = {}
pokemon_name = {}
for i in range(1,1+n):
    name = input()
    pokemon_num[i] = name
    pokemon_name[name] = i
for _ in range(m):
    problem = input()
    if problem.isdigit():
        print(pokemon_num[int(problem)])
    else:
        print(pokemon_name[problem])