import sys
from collections import deque


T = int(input())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    que = deque()
    que.append(A)
    vis = [0]*10000
    vis[A] = 'A'
    if A == B:
        res = ""
    else:
        while que:
            i = que.popleft()
            cnum = (2*i) % 10000
            if vis[cnum] == 0:
                if cnum == B:
                    res = vis[i][1:]+"D"
                    break
                else:
                    vis[cnum] = vis[i]+"D"
                    que.append(cnum)
            if i == 0:
                cnum = 9999
            else:
                cnum = i-1
            if vis[cnum] == 0:
                if cnum == B:
                    res = vis[i][1:]+"S"
                    break
                else:
                    vis[cnum] = vis[i]+"S"
                    que.append(cnum)
            temp = i//1000
            cnum = (i-temp*1000)*10
            cnum += temp
            if vis[cnum] == 0:
                if cnum == B:
                    res = vis[i][1:]+"L"
                    break
                else:
                    vis[cnum] = vis[i]+"L"
                    que.append(cnum)
            temp = i % 10
            cnum = i//10
            cnum += temp*1000
            if vis[cnum] == 0:
                if cnum == B:
                    res = vis[i][1:]+"R"
                    break
                else:
                    vis[cnum] = vis[i]+"R"
                    que.append(cnum)

    print(res)
