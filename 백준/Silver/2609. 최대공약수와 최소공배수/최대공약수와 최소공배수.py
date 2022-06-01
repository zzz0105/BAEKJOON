x, y = map(int, input().split())
z = x * y
while y: x, y = y, x % y
print(x)          
print(int(z/x))   