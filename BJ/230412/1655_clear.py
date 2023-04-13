import heapq
import sys

N = int(input())
shea = []
bhea = []
num = 'none'
for _ in range(N):
    n = int(sys.stdin.readline())
    if num == 'none':
        num = n
    elif num > n:
        heapq.heappush(shea, (-n, n))
    else:
        heapq.heappush(bhea, n)
    if len(shea) > len(bhea):
        heapq.heappush(bhea, num)
        num = heapq.heappop(shea)[1]
    elif len(shea)+1 < len(bhea):
        heapq.heappush(shea, (-num, num))
        num = heapq.heappop(bhea)
    print(num)
