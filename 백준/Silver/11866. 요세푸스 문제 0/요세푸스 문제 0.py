n, k = map(int,input().split())
people = [i for i in range(1,n+1)]
now = 0
print('<', end='')
while len(people)!=1:
    now = (now + k - 1) % len(people)
    print(people[now], end=', ')
    del people[now]
print(people.pop(), end='')
print('>')