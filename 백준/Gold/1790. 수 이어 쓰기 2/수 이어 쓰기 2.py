N, k = map(int,input().split())
# N까지의 수 이어쓰기, k번째 수
total = 0
digit = 1   # 자릿수

while True:
    ea = 9 * 10**(digit-1) # digit의 자릿수를 가진 수의 개수
    length = digit * ea
    if k <= length: break
    k -= length
    digit += 1
    total += ea

answer = (total+1) + (k-1)//digit

print(-1 if answer>N else str(answer)[(k-1)%digit])