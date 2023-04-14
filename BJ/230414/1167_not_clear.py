import sys
from collections import deque
sys.setrecursionlimit(100000)


def dfs(i, prev):
    vdis = 0
    for j in dic[i]:
        if j[0] == prev:
            continue
        vdis = max(vdis, dfs(j[0], i)+j[1])
    return vdis


V = int(input())

dic = {}
vli = []
tli = []
for _ in range(V):
    inp = [int(x) for x in sys.stdin.readline().split()]
    inpset = []
    for i in range(1, len(inp)-2, 2):
        inpset.append((inp[i], inp[i+1]))
    if len(inpset) == 1:
        vli.append(inp[0])
    elif len(inpset) == 2:
        tli.append(inp[0])
    dic[inp[0]] = inpset

for i in tli:
    leng = dic[i][0][1]+dic[i][1][1]
    for j in range(2):
        dic[dic[i][j][0]].remove((i, dic[i][j][1]))
        dic[dic[i][j][0]].append((dic[i][1-j][0], leng))
    dic.pop(i)

dis = 0
for i in vli:
    dis = max(dis, dfs(i, 0))

print(dis)
