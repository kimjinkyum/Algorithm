from collections import deque

def solution(queue1, queue2):
    
    total_sum = sum(queue1) + sum(queue2)
    answer = 0
    
    if total_sum % 2 == 1:
        return -1
    target = total_sum // 2
    
    queue1_sum = sum(queue1)
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while queue1 and queue2:
        if queue1_sum > target:
            value = queue1.popleft()
            queue1_sum -= value
        elif queue1_sum < target:
            value = queue2.popleft()
            queue1_sum += value
            queue1.append(value)
        
        else:
            return answer
        
        answer +=1
    
    return -1
