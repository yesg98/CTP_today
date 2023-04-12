# 힙 구현용 함수
# 최대값 제거
def maxpop(maxList, minList):
    if len(maxList) > 0:
        if len(maxList) > 1:
            maxList[0], maxList[len(
                maxList)-1] = maxList[len(maxList)-1], maxList[0]
            maxList.pop()
            n = 0
            while True:
                if 2*n+1 < len(maxList):
                    if 2*n+2 < len(maxList):
                        if maxList[2*n+1] >= maxList[2*n+2]:
                            if maxList[0] < maxList[2*n+1]:
                                maxList[0], maxList[2*n +
                                                    1] = maxList[2*n+1], maxList[0]
                                n = 2*n+1
                            else:
                                break
                        else:
                            if maxList[0] < maxList[2*n+2]:
                                maxList[0], maxList[2*n +
                                                    2] = maxList[2*n+2], maxList[0]
                                n = 2*n+2
                            else:
                                break
                    else:
                        if maxList[0] < maxList[2*n+1]:
                            maxList[0], maxList[2*n +
                                                1] = maxList[2*n+1], maxList[0]
                            n = 2*n+1
                        else:
                            break
                else:
                    break
        else:
            maxList.pop()
            minList.pop()
    return maxList, minList
# 최소값 제거


def minpop(List):
    if len(List) > 0:
        if len(List) > 1:
            List[0], List[len(List)-1] = List[len(List)-1], List[0]
            List.pop()
            n = 0
            while True:
                if 2*n+1 < len(List):
                    if 2*n+2 < len(List):
                        if List[2*n+1] <= List[2*n+2]:
                            if List[0] > List[2*n+1]:
                                List[0], List[2*n+1] = List[2*n+1], List[0]
                                n = 2*n+1
                            else:
                                break
                        else:
                            if List[0] > List[2*n+2]:
                                List[0], List[2*n+2] = List[2*n+2], List[0]
                                n = 2*n+2
                            else:
                                break
                    else:
                        if List[0] > List[2*n+1]:
                            List[0], List[2*n+1] = List[2*n+1], List[0]
                            n = 2*n+1
                        else:
                            break
                else:
                    break
        else:
            List.pop()
    return List


def queins(List, n):

    # 테스트 케이스 개수 입력
T = int(input())

# 테스트 수행
for _ in range(T):

    # 연산 수 입력
    N = int(input())

    # 우선순위 큐 만들기
    maxlist = []
    minlist = []

    # 명령 입력
    for a in range(N):
        com = input().split()
