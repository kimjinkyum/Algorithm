from collections import Counter

def check_finish(board, flag):
    
    for i in range(3):
        if board[i] == flag * 3:
            return True
        tmp = "".join(board[j][i] for j in range(3))
        if tmp == flag*3:
            return True
    
    
    if board[0][0] + board[1][1] + board[2][2] == flag*3:
        return True
    if board[2][0] + board[1][1] + board[0][2] == flag*3:
        return True
    
    return False
def solution(board):
    answer = 1
    count_dict = {'O':0, 'X':0}
    
    for bo in board:
        count = Counter(bo)
        count_dict['O'] +=count['O']
        count_dict['X'] +=count['X']

    
    
    if count_dict['O'] == 0 and count_dict['X'] == 0:
        answer = 1
        return answer
    
    
    if count_dict['X'] > count_dict['O']:
        answer = 0
    
    if count_dict['O'] - count_dict['X'] > 1:
        answer = 0
        return answer

    if count_dict['O'] > count_dict['X']:
        if check_finish(board, 'O'):
            if check_finish(board, 'X'):
                answer = 0
        else:
            if check_finish(board, 'X'):
                answer = 0
    if count_dict['O'] == count_dict['X']:
        if check_finish(board, 'O'):
            answer = 0
                
    return answer