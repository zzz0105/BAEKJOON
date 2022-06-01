heights = []    #난쟁이들의 키
for _ in range(9):
    heights += [int(input())]
no_dwarf = sum(heights) - 100  #난쟁이가 아닌 사람들의 키의 합
for height1 in heights:
    for height2 in heights:
        if height1 != height2 and (height1+height2) == no_dwarf:
            heights.remove(height1)
            heights.remove(height2)
            break
    if len(heights) == 7: #위에서 난쟁이가 아닌 사람들이 제거되었으면
        break

heights.sort()
for height in heights:
    print(height)
