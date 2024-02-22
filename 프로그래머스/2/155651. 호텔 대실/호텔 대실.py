def change_to_mininute(book_time):
    result = []
    for start, end in book_time:
        s = start.split(":")
        e = end.split(":")
        
        result.append([int(s[0]) * 60 + int(s[1]), int(e[0]) * 60 + int(e[1]) + 10])
    
    return result
        
def find_min(occupy):
    min_value = occupy[0]
    min_idx = 0
    for idx, o in enumerate(occupy):
        if min_value > o:
            min_value = o
            min_idx = idx
    
    return min_idx, min_value
    
def solution(book_time):
    answer = 0
    
    book_time = sorted(book_time)
    
    rooms = change_to_mininute(book_time)
    # print(rooms)
    occupy = [rooms[0][1]]
    # print(occupy)
    for room in rooms[1:]:
        
        idx, min_end = find_min(occupy)
        if room[0] < min_end:
            occupy.append(room[1])
        else:
            occupy[idx] = room[1]
    
    answer = len(occupy)
    return answer