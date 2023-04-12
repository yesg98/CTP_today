# 지역 입력
N = int(input())

# 지도 입력
Map = [list(input()) for _ in range(N)]

# DFS 함수 생성


def dfs(a, b):
    Map[a][b] = '0'
    ret = 1
    if a > 0 and Map[a-1][b] == '1':
        ret += dfs(a-1, b)
    if b > 0 and Map[a][b-1] == '1':
        ret += dfs(a, b-1)
    if a < N-1:
        if Map[a+1][b] == '1':
            ret += dfs(a+1, b)
    if b < N-1:
        if Map[a][b+1] == '1':
            ret += dfs(a, b+1)
    return ret


# 함수를 사용한 단지 구별
res = 0
reslist = []
for i in range(N):
    for j in range(N):
        if Map[i][j] == '1':
            res += 1
            reslist.append(dfs(i, j))
print(res)
reslist.sort()
for i in reslist:
    print(i)
