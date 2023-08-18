def clean(time):
    h, m = map(int, time.split(":"))
    if m >= 50: h += 1; m -= 60
    h, m = str(h), str(m+10)
    return "0"*(2-len(h))+h +":"+ "0"*(2-len(m))+m

def solution(book_time):
    book_time.sort()
    room = ["00:00"]*len(book_time)
    for s,e in book_time:
        for i in range(len(room)):
            if room[i] <= s:
                room[i] = clean(e)
                break
    return len(book_time) - room.count("00:00")