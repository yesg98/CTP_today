import sys
N, M = map(int, input().split())
List = [int(x) for x in input().split()]
Lisum = [0]*(N+1)
num = 0
for i in range(N):
    num += List[i]
    Lisum[i+1] = num

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    print(Lisum[b]-Lisum[a])
