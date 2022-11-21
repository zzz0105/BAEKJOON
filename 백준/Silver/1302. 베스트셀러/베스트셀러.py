n = int(input())
books = {}
for _ in range(n):
    tmp = input()
    books[tmp] = books.get(tmp, 0) + 1
print(sorted(books.items(), key=lambda x:(-x[1], x[0]))[0][0])