import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    List = [set() for a in range(N+1)]
    for i in range(M):
        S, E, T = map(int, input().split())
        List[S].add((E, T))
        List[E].add((S, T))
    for i in range(W):
        S, E, T = map(int, input().split())
        List[S].add((E, -1*T))

    res = False
    dt = [50000001]*(N+1)
    dt[1] = 0
    for re in range(N):
        for j in range(1, N+1):
            for t in List[j]:
                if dt[t[0]] > dt[j]+t[1]:
                    dt[t[0]] = dt[j]+t[1]
                    if re == N-1:
                        res = True
                        break
    if res:
        print("YES")
    else:
        print("NO")
