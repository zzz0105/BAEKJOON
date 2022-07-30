def solution(sizes):
    w, h = 0,0
    for size in sizes:
        if w < size[0] or h < size[1]:
            if w < size[1] or h < size[0]:
                w = max(w, min(size[0], size[1]))
                h = max(h, max(size[0], size[1]))            
    return w*h