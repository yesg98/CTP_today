# M,N값 받기
a, b = map(int, input().split())

# 미로 받기
List = []
for _ in range(a):
    List.append(list(map(int, list(input()))))

# 너비우선탐색
res = 1
road = [[0, 0]]
List[0][0] = 0
nextroad = []

while True:
    for i in road:
        x = i[0]
        y = i[1]
        if x == a-1 and y == b-1:
            break
        if x > 0 and List[x-1][y] == 1:
            nextroad.append([x-1, y])
            List[x-1][y] = 0
        if y > 0 and List[x][y-1] == 1:
            nextroad.append([x, y-1])
            List[x][y-1] = 0
        if x+1 < a:
            if List[x+1][y] == 1:
                nextroad.append([x+1, y])
                List[x+1][y] = 0
        if y+1 < b:
            if List[x][y+1] == 1:
                nextroad.append([x, y+1])
                List[x][y+1] = 0
    if x == a-1 and y == b-1:
        break
    res += 1
    road = nextroad.copy()
    nextroad.clear()

print(res)
