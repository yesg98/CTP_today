import sys
from collections import deque
sys.setrecursionlimit(100000)


def dfs(i):
    vdis = []
    dis = 0
    for j in dic[i]:
        if len(dic[j[0]]) == 1:
            vdis.append(j[1])
            continue
        if j[0] in vis:
            continue
        vis.add(j[0])
        a, b = dfs(j[0])
        dis = max(dis, a)
        vdis.append(b+j[1])
    if len(vdis) == 1:
        return vdis[0]
    vdis.sort(reverse=True)
    return max(dis, vdis[0]+vdis[1]), vdis[0]


V = int(input())

dic = {}
vli = []
tli = []
thli = []
for _ in range(V):
    inp = [int(x) for x in sys.stdin.readline().split()]
    inpset = set()
    for i in range(1, len(inp)-2, 2):
        inpset.add((inp[i], inp[i+1]))
    if len(inpset) == 1:
        vli.append(inp[0])
    elif len(inpset) == 2:
        tli.append(inp[0])
    else:
        thli.append(inp[0])
    dic[inp[0]] = inpset

for i in tli:
    leng = 0
    li = []
    for j in dic[i]:
        leng += j[1]
        li.append(j)
    for j in range(2):
        dic[li[j][0]].remove((i, li[j][1]))
        dic[li[j][0]].add((li[1-j][0], leng))
    dic.pop(i)

if len(thli) == 0:
    dis = dfs(vli[0])
else:
    vis = set()
    vis.add(thli[0])
    dis = dfs(thli[0])[0]

print(dis)
