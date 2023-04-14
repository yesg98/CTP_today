from collections import deque


def bfs():
    que = deque()
    vis = []
    que.append((1, 0))
    res = 0
    while que:
        po = que.popleft()
        flag = False
        for i in range(1, 7):
            ch = True
            num = po[0]+i
            if num == 100:
                res = po[1]+1
                flag = True
                break
            if num in vis:
                continue
            for j in A:
                if num == j[0]:
                    vis.append(num)
                    num = j[1]
                    ch = False
                    break
            if ch:
                for j in B:
                    if num == j[0]:
                        vis.append(num)
                        num = j[1]
                        break
            vis.append(num)
            que.append((num, po[1]+1))
        if flag:
            break
    return res


a, b = map(int, input().split())
A = []
B = []
for _ in range(a):
    A.append([int(x) for x in input().split()])
for _ in range(b):
    B.append([int(x) for x in input().split()])

print(bfs())
