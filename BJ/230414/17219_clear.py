import sys
N, M = map(int, input().split())
dic = {}
for _ in range(N):
    inp = sys.stdin.readline().split()
    dic[inp[0]] = inp[1]
for _ in range(M):
    inp = sys.stdin.readline()
    print(dic[inp.rstrip()])
