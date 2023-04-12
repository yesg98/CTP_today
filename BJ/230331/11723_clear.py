import sys
List = [0 for x in range(21)]

N = int(input())

for _ in range(N):
    com = sys.stdin.readline().split()
    if com[0]=="add":
        List[int(com[1])] = 1
    elif com[0]=="remove":
        List[int(com[1])] = 0
    elif com[0]=="check":
        print(List[int(com[1])])
    elif com[0]=="toggle":
        if List[int(com[1])]==1:
            List[int(com[1])] = 0
        else:
            List[int(com[1])] = 1
    elif com[0]=="all":
        for x in range(21):
            List[x] = 1
    else:
        for x in range(21):
            List[x] = 0