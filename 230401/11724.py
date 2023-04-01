import sys

N, M = map(int, input().split())

num_list = [[int(x)] for x in range(N+1)]

res = N

for _ in range(M):
    com = sys.stdin.readline().split()
    a = int(min(com))
    b = int(max(com))
    for i in range(N+1):
        if num_list[i] == -1:
            continue
        if a in num_list[i]:
            if b in num_list[i]:
                break
            else:
                if num_list[b] == -1:
                    for j in range(N+1):
                        if num_list[j] == -1:
                            continue
                        if b in num_list[j]:
                            num_list[i] += num_list[j]
                            num_list[j] = -1
                            res -= 1
                            break
                else:
                    num_list[i] += num_list[b]
                    num_list[b] = -1
                    res -= 1
                    break
            break

print(res)
