from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    
    for c in counter.most_common():
        k -= c[1]
        answer +=1
        if k <=0 :
            break
        

    return answer