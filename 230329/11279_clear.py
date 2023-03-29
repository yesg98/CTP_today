import sys


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
        return 0
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


T = int(input())
List = []
for _ in range(T):
    num = int(sys.stdin.readline())
    if num:
        maxqueins(List, num)
    else:
        print(maxpop(List))
