def find(i, j):
    num = 0
    # num = max(num,())
    # ㅣ
    if i < N-3:
        num = max(num, (List[i][j]+List[i+1][j]+List[i+2][j]+List[i+3][j]))
    if j < M-3:
        num = max(num, (List[i][j]+List[i][j+1]+List[i][j+2]+List[i][j+3]))
    # ㅁ
    if i < N-1 and j < M-1:
        num = max(num, (List[i][j]+List[i+1][j]+List[i][j+1]+List[i+1][j+1]))
    # ㅜ
    if i < N-1 and j < M-1 and j > 0:
        num = max(num, (List[i][j-1]+List[i][j]+List[i][j+1]+List[i+1][j]))
    # ㅓ
    if i > 0 and i < N-1 and j > 0:
        num = max(num, (List[i][j]+List[i-1][j]+List[i+1][j]+List[i][j-1]))
    # ㅗ
    if i > 0 and j > 0 and j < M-1:
        num = max(num, (List[i][j]+List[i-1][j]+List[i][j-1]+List[i][j+1]))
    # ㅏ
    if i > 0 and j < M-1 and i < N-1:
        num = max(num, (List[i][j]+List[i-1][j]+List[i][j+1]+List[i+1][j]))
    # z
    if i < N-2 and j < M-1:
        num = max(num, (List[i][j]+List[i+1][j]+List[i+1][j+1]+List[i+2][j+1]))
    if i < N-2 and j > 0:
        num = max(num, (List[i][j]+List[i+1][j]+List[i+1][j-1]+List[i+2][j-1]))
    if i > 0 and j < M-2:
        num = max(num, (List[i][j]+List[i][j+1]+List[i-1][j+1]+List[i-1][j+2]))
    if i < N-1 and j < M-2:
        num = max(num, (List[i][j]+List[i][j+1]+List[i+1][j+1]+List[i+1][j+2]))
    # L
    if i < N-2 and j < M-1:
        num = max(num, (List[i][j]+List[i+1][j]+List[i+2][j]+List[i+2][j+1]))
    if i < N-2 and j > 0:
        num = max(num, (List[i][j]+List[i+1][j]+List[i+2][j]+List[i+2][j-1]))
    if i > 0 and j < M-2:
        num = max(num, (List[i][j]+List[i][j+1]+List[i][j+2]+List[i-1][j+2]))
    if i < N-1 and j < M-2:
        num = max(num, (List[i][j]+List[i][j+1]+List[i][j+2]+List[i+1][j+2]))
    if i > 0 and j > 1:
        num = max(num, (List[i][j]+List[i][j-1]+List[i][j-2]+List[i-1][j-2]))
    if i < N-1 and j > 1:
        num = max(num, (List[i][j]+List[i][j-1]+List[i][j-2]+List[i+1][j-2]))
    if i > 1 and j < M-1:
        num = max(num, (List[i][j]+List[i-1][j]+List[i-2][j]+List[i-2][j+1]))
    if i > 1 and j > 0:
        num = max(num, (List[i][j]+List[i-1][j]+List[i-2][j]+List[i-2][j-1]))
    return num


N, M = map(int, input().split())

List = []
for _ in range(N):
    List.append([int(x) for x in input().split()])

res = 0

for i in range(N):
    for j in range(M):
        res = max(res, find(i, j))
print(res)
