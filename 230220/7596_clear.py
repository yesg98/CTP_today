# M,N,H 입력
M, N, H = map(int, input().split())

# 상자 리스트 생성
List = []
for _ in range(H):
    box = []
    for a in range(N):
        box.append(input().split())
    List.append(box)
# 익은 토마토 좌표 저장
now = []
for i in range(M):
    for j in range(N):
        for k in range(H):
            if List[k][j][i] == '1':
                now.append([k, j, i])

# 알고리즘 시작
n = 0
nextlist = []
while True:
    for a in now:
        x = a[0]
        y = a[1]
        z = a[2]
        if x > 0 and List[x-1][y][z] == '0':
            List[x-1][y][z] = '1'
            nextlist.append([x-1, y, z])
        if y > 0 and List[x][y-1][z] == '0':
            List[x][y-1][z] = '1'
            nextlist.append([x, y-1, z])
        if z > 0 and List[x][y][z-1] == '0':
            List[x][y][z-1] = '1'
            nextlist.append([x, y, z-1])
        if x < H-1:
            if List[x+1][y][z] == '0':
                List[x+1][y][z] = '1'
                nextlist.append([x+1, y, z])
        if y < N-1:
            if List[x][y+1][z] == '0':
                List[x][y+1][z] = '1'
                nextlist.append([x, y+1, z])
        if z < M-1:
            if List[x][y][z+1] == '0':
                List[x][y][z+1] = '1'
                nextlist.append([x, y, z+1])
    if len(nextlist) == 0:
        break
    else:
        n += 1
        now = nextlist.copy()
        nextlist.clear()
# 모든 토마토 익었는지 확인
sta = True
for i in List:
    for j in i:
        for k in j:
            if k == '0':
                sta = False
# 출력
if sta:
    print(n)
else:
    print(-1)
