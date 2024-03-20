def solution(board, h, w):
    answer = 0 
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    n = len(board) -1 
    curr = board[h][w]
    for i in range(4):
        dx = h + dh[i]
        dy = w + dw[i]
        if dx > n or dy > n or dx < 0 or dy < 0:
            continue
        if curr == board[dx][dy]:
            answer +=1
    
    return answer