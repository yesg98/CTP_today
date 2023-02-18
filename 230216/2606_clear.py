# 컴퓨터 대수 입력
N = int(input())

# 연결선개수 입력
connection = int(input())

# 연결 입력
connect = [[] for _ in range(N+1)]
for _ in range(connection):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

# 너비우선탐색
reslist = [1]
now = connect[1].copy()
nextlist = []
while True:
    if len(now) == 0:
        break
    for i in now:
        if i not in reslist:
            reslist.append(i)
            for j in connect[i]:
                if j not in nextlist:
                    nextlist.append(j)
    now = nextlist.copy()
    nextlist.clear()

print(len(reslist)-1)
