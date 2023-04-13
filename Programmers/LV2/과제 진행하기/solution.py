def solution(plans):
    answer = []
    studyStack = []
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(':'))
        plans[i][1] = h*60+m
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1])

    for i in range(len(plans)-1):
        if plans[i+1][1]-plans[i][1] >= plans[i][2]:
            freeTime = plans[i+1][1]-plans[i][1]-plans[i][2]
            answer.append(plans[i][0])
            while freeTime > 0 and len(studyStack) > 0:
                po = studyStack.pop()
                if freeTime >= po[1]:
                    freeTime -= po[1]
                    answer.append(po[0])
                else:
                    po[1] -= freeTime
                    freeTime = 0
                    studyStack.append(po)
        else:
            studyStack.append(
                [plans[i][0], plans[i][2]-(plans[i+1][1]-plans[i][1])])

    answer.append(plans[-1][0])
    while len(studyStack) > 0:
        po = studyStack.pop()
        answer.append(po[0])

    return answer
