n = int(input())
sang = set(map(int,input().split()))
m = int(input())
cards = map(int,input().split())
for card in cards:
    print(1 if card in sang else 0, end=' ')