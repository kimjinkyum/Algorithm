def solution(plans):
    answer = []
    for plan in plans:
        hh = plan[1].split(":")[0]
        mm = plan[1].split(":")[1]
        plan[1] = int(hh)* 60 + int(mm)
    
    plans.sort(key=lambda x : x[1])
    
    pause_homework = []

    for idx in range(len(plans)-1):
        plans[idx][2] = int(plans[idx][2])
        during_time = plans[idx+1][1] - plans[idx][1]
        times = min(during_time, (plans[idx][2]))
        plans[idx][2] -= times
        
        # 과제를 못끝낸 경우 (pause에 들어가기)
        if plans[idx][2] > 0:
            pause_homework.append(idx)
        # 과제를 끝난 경우 확인
        else:
            answer.append(plans[idx][0])
            # 쓸 수 있는 시간이 더 길면..?
            if during_time > times:
                spend_time = during_time - times
                while pause_homework:
                    pause_idx = pause_homework.pop()
                    tmp = min(spend_time, plans[pause_idx][2])
                    plans[pause_idx][2]-= tmp
                    if plans[pause_idx][2] == 0:
                        answer.append(plans[pause_idx][0])
                    else:
                        pause_homework.append(pause_idx)
                    spend_time -= tmp
                    if spend_time == 0:
                        break

    answer.append(plans[-1][0])
    while pause_homework:
        answer.append(plans[pause_homework.pop()][0])


    
    return answer