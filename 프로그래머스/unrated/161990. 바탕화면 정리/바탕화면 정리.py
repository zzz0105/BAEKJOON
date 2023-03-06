def solution(wallpaper):
    h, w = len(wallpaper), len(wallpaper[0])
    lux, luy, rdx, rdy = h, w, 0, 0
    for i in range(h):
        for j in range(w):
            if wallpaper[i][j]=='#':
                lux = min(lux,i)
                luy = min(luy,j)
                rdx = max(rdx,i+1)
                rdy = max(rdy,j+1)
    return [lux, luy, rdx, rdy]