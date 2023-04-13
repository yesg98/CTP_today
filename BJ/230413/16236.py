from collections import deque


def shark(lo, power):
    vis = [lo]
    res = []
    flag = 401
    que = deque()
    que.append((0, lo))
    while que:
        po = que.popleft()
        if po[0] >= flag:
            break
        x = po[1][0]
        y = po[1][1]
        if x > 0 and [x-1, y] not in vis:
            if List[x-1][y] > 0 and List[x-1][y] < power:
                flag = po[0]+1
                res.append([x-1, y])
                vis.append([x-1, y])
            elif List[x-1][y] == power or List[x-1][y] == 0:
                que.append((po[0]+1, [x-1, y]))
                vis.append([x-1, y])
        if y > 0 and [x, y-1] not in vis:
            if List[x][y-1] > 0 and List[x][y-1] < power:
                flag = po[0]+1
                res.append([x, y-1])
                vis.append([x, y-1])
            elif List[x][y-1] == power or List[x][y-1] == 0:
                que.append((po[0]+1, [x, y-1]))
                vis.append([x, y-1])
        if x < N-1 and [x+1, y] not in vis:
            if List[x+1][y] > 0 and List[x+1][y] < power:
                flag = po[0]+1
                res.append([x+1, y])
                vis.append([x+1, y])
            elif List[x+1][y] == power or List[x+1][y] == 0:
                que.append((po[0]+1, [x+1, y]))
                vis.append([x+1, y])
        if y < N-1 and [x, y+1] not in vis:
            if List[x][y+1] > 0 and List[x][y+1] < power:
                flag = po[0]+1
                res.append([x, y+1])
                vis.append([x, y+1])
            elif List[x][y+1] == power or List[x][y+1] == 0:
                que.append((po[0]+1, [x, y+1]))
                vis.append([x, y+1])
    res.sort(key=lambda x: (x[0], x[1]))
    if res:
        return (flag, res[0])
    else:
        return "call mom"


N = int(input())
List = []
feed = [0]*7
for _ in range(N):
    List.append([int(x) for x in input().split()])

for i in range(N):
    for j in range(N):
        if List[i][j] == 9:
            now = [[i, j], 2]
            List[i][j] = 0
        elif List[i][j] > 0:
            feed[List[i][j]] += 1
Time = 0
eat = 0
while sum(feed[:now[1]]) > 0:
    feedTime = shark(now[0], now[1])
    if feedTime == "call mom":
        break
    else:
        eat += 1
        now = [feedTime[1], now[1]]
        feed[List[now[0][0]][now[0][1]]] -= 1
        List[now[0][0]][now[0][1]] = 0
        if eat == now[1]:
            now[1] += 1
            eat = 0
        Time += feedTime[0]
print(Time)
