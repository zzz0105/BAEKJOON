n, m = map(int, input().split())
#math.gcd와 math.lcm을 사용하면 최대공약수 최소공배수 한방에 구할 수 있다

#유클리드 호제법 이용해서 최대공약수 구하기
x, y = n, m

while True:
    r = x % y
    x, y = y, r
    if r==0: break
    
print(x)            #최대공약수
print(int(n*m/x))   #최소공배수