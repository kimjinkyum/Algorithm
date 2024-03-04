import math
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True
def convert_n(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n, k):
    answer = 0
    
    n = convert_n(n, k)
    
    for sub in str(n).split('0'):
        if sub and is_prime(int(sub)):
            answer +=1
    
    return answer