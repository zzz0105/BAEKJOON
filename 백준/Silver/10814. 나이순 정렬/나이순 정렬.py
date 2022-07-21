n = int(input())
users = []
for i in range(n):
    age, name = input().split()
    users.append((int(age), name, i))
users = sorted(users, key= lambda x : (x[0], x[2]))
for j in range(n):
    print(users[j][0], users[j][1])