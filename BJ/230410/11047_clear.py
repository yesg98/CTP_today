N, K = map(int, input().split())
List = [0]*N
res = 0
for i in range(N):
    inp = int(input())
    List[N-i-1] = inp

for i in List:
    if i > K:
        continue
    res += K//i
    K = K % i
print(res)
