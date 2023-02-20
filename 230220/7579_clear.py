# M,N,H 입력
M, N = map(int, input().split())

# 상자 리스트 생성
List = []
for a in range(N):
    List.append(input().split())
# 익은 토마토 좌표 저장
now = []
for i in range(M):
    for j in range(N):
        if List[j][i] == '1':
            now.append([j, i])

# 알고리즘 시작
n = 0
nextlist = []
while True:
    for a in now:
        x = a[0]
        y = a[1]
        if x > 0 and List[x-1][y] == '0':
            List[x-1][y] = '1'
            nextlist.append([x-1, y])
        if y > 0 and List[x][y-1] == '0':
            List[x][y-1] = '1'
            nextlist.append([x, y-1])
        if x < N-1:
            if List[x+1][y] == '0':
                List[x+1][y] = '1'
                nextlist.append([x+1, y])
        if y < M-1:
            if List[x][y+1] == '0':
                List[x][y+1] = '1'
                nextlist.append([x, y+1])
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
        if j == '0':
            sta = False
# 출력
if sta:
    print(n)
else:
    print(-1)
