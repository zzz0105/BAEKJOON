D, H, W = map(int,input().split())
r = (D*D/(H*H+W*W))**0.5
print(int(r*H), int(r*W))