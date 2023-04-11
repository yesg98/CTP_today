import sys
sys.setrecursionlimit(10000)

def dfs(li, i, j):
    temp = li[i][j]
    li[i][j] = 0
    if i > 0:
        if li[i-1][j] == temp:
            dfs(li, i-1, j)
    if i < len(li)-1:
        if li[i+1][j] == temp:
            dfs(li, i+1, j)
    if j > 0:
        if li[i][j-1] == temp:
            dfs(li, i, j-1)
    if j < len(li[0])-1:
        if li[i][j+1] == temp:
            dfs(li, i, j+1)


N = int(input())

reg = []
wreg = []
res = 0
wres = 0

for _ in range(N):
    inp = input()
    reg.append(list(inp))
    wreg.append(list(inp.replace('R', 'G')))

for i in range(N):
    for j in range(N):
        if reg[i][j] != 0:
            res += 1
            dfs(reg, i, j)
        if wreg[i][j] != 0:
            wres += 1
            dfs(wreg, i, j)
print(res, wres)
