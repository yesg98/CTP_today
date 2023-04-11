import sys
import heapq
from collections import deque
N = int(input())
hea = []
que = deque()
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        que.clear()
        flag = True
        while len(hea) > 0:
            po = heapq.heappop(hea)
            if len(que) == 0:
                if po[1] < 0:
                    print(po[1])
                    flag = False
                    break
                else:
                    que.append(po)
            else:
                if po[0] == que[0][0]:
                    if po[1] < 0:
                        print(po[1])
                        flag = False
                        break
                    else:
                        que.append(po)
                else:
                    que.append(po)
                    break
        if flag:
            if que:
                res = que.popleft()
                print(res[1])
            else:
                print(0)
        while que:
            heapq.heappush(hea, que.popleft())
    else:
        heapq.heappush(hea, (abs(num), num))
