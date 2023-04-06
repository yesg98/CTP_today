T = int(input())

for _ in range(T):
    N = int(input())
    dic = {}
    for i in range(N):
        inp = input().split()
        if inp[1] in dic:
            dic[inp[1]] += 1
        else:
            dic[inp[1]] = 1
    List = dic.keys()
    res = 0
    for j in List:
        res += (res+1)*dic[j]
    print(res)
