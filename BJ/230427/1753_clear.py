import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
st = int(input())

dic = {}
for i in range(v):
    dic[i+1] = []
for _ in range(e):
    a, b, c = map(int, input().split())
    dic[a].append((b, c))

List = ["INF"]*v
List[st-1] = 0
vis = set()
hea = []
heapq.heappush(hea, (0, st))

while hea:
    po = heapq.heappop(hea)
    if po[1] in vis:
        continue
    vis.add(po[1])
    nowLeng = po[0]
    nowLo = po[1]
    for i in dic[nowLo]:
        leng = nowLeng+i[1]
        lo = i[0]
        if List[lo-1] == "INF" or List[lo-1] > leng:
            List[lo-1] = leng
            heapq.heappush(hea, (leng, lo))
for i in List:
    print(i)
