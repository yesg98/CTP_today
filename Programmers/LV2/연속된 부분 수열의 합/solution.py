def solution(sequence, k):
    answer = []
    start = 0
    end = 1
    sumList = [0]*(len(sequence)+1)
    sumNum = 0
    for i in range(len(sequence)):
        if sequence[i]<=k:
            sumNum += sequence[i]
            sumList[i+1] = sumNum
        else:
            break
    resList = []
    while end<=len(sequence):
        num = sumList[end]-sumList[start]
        if num==k:
            resList.append([end-start-1,start,end-1])
            end+=1
        elif num<k:
            end+=1
        else:
            start+=1
    resList.sort(key=lambda x : (x[0],x[1]))
    answer = resList[0][1:]
        
    
    return answer