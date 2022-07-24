def solution(genres, plays):
    music = {}
    sums = {}
    album = []
    for i in range(len(genres)):
        music[genres[i]] = music.get(genres[i], []) + [(i, plays[i])]
        sums[genres[i]] = sums.get(genres[i], 0) + plays[i]
    sums = sorted(sums, key=lambda x:sums[x], reverse=True)
    
    for s in sums:
        tmp = sorted(music[s], key=lambda x:(x[1],-x[0]), reverse=True)
        for i in range(2):
            album.append(tmp[i][0])
            if len(music[s]) < 2:
                break
                
    return album