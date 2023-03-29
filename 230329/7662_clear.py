import sys
# 힙 구현용 함수
# 최대값 제거


def maxpop(maxList):
    if len(maxList) > 0:
        if len(maxList) > 1:
            maxList[0], maxList[len(
                maxList)-1] = maxList[len(maxList)-1], maxList[0]
            num = maxList.pop()
            n = 0
            while True:
                if 2*n+1 < len(maxList):
                    if 2*n+2 < len(maxList):
                        if maxList[2*n+1] >= maxList[2*n+2]:
                            if maxList[n] < maxList[2*n+1]:
                                maxList[n], maxList[2*n +
                                                    1] = maxList[2*n+1], maxList[n]
                                n = 2*n+1
                            else:
                                break
                        else:
                            if maxList[n] < maxList[2*n+2]:
                                maxList[n], maxList[2*n +
                                                    2] = maxList[2*n+2], maxList[n]
                                n = 2*n+2
                            else:
                                break
                    else:
                        if maxList[n] < maxList[2*n+1]:
                            maxList[n], maxList[2*n +
                                                1] = maxList[2*n+1], maxList[n]
                            n = 2*n+1
                        else:
                            break
                else:
                    break
        else:
            num = maxList.pop()
    else:
        return "empty"
    return num
# 최소값 제거


def minpop(List):
    if len(List) > 0:
        if len(List) > 1:
            List[0], List[len(List)-1] = List[len(List)-1], List[0]
            num = List.pop()
            n = 0
            while True:
                if 2*n+1 < len(List):
                    if 2*n+2 < len(List):
                        if List[2*n+1] <= List[2*n+2]:
                            if List[n] > List[2*n+1]:
                                List[n], List[2*n+1] = List[2*n+1], List[n]
                                n = 2*n+1
                            else:
                                break
                        else:
                            if List[n] > List[2*n+2]:
                                List[n], List[2*n+2] = List[2*n+2], List[n]
                                n = 2*n+2
                            else:
                                break
                    else:
                        if List[n] > List[2*n+1]:
                            List[n], List[2*n+1] = List[2*n+1], List[n]
                            n = 2*n+1
                        else:
                            break
                else:
                    break
        else:
            num = List.pop()
    else:
        return "empty"
    return num


def maxqueins(List, n):
    List.append(n)
    i = (len(List)-1)
    p = (i-1)//2
    while p >= 0:
        if List[p] < List[i]:
            List[i], List[p] = List[p], List[i]
            i = p
            p = (i-1)//2
        else:
            break


def minqueins(List, n):
    List.append(n)
    i = (len(List)-1)
    p = (i-1)//2
    while p >= 0:
        if List[p] > List[i]:
            List[i], List[p] = List[p], List[i]
            i = p
            p = (i-1)//2
        else:
            break


# 테스트 케이스 개수 입력
T = int(input())

# 테스트 수행
for _ in range(T):

    # 연산 수 입력
    N = int(input())

    # 우선순위 큐 만들기
    maxlist = []
    minlist = []

    dic = {}
    dic["empty"] = 1

    # 명령 입력
    for a in range(N):
        com = sys.stdin.readline().split()
        if com[0] == 'I':
            num = int(com[1])
            maxqueins(maxlist, num)
            minqueins(minlist, num)
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        else:
            if com[1] == "1":
                num = maxpop(maxlist)
                while dic[num] == 0:
                    num = maxpop(maxlist)
                if num == "empty":
                    continue
                dic[num] -= 1
            else:
                num = minpop(minlist)
                while dic[num] == 0:
                    num = minpop(minlist)
                if num == "empty":
                    continue
                dic[num] -= 1

    anum = maxpop(maxlist)
    while dic[anum] == 0:
        anum = maxpop(maxlist)
    inum = minpop(minlist)
    while dic[inum] == 0:
        inum = minpop(minlist)
    if anum == "empty":
        print('EMPTY')
    else:
        print(anum, inum)
