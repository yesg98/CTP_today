N = int(input())

List = [int(x) for x in input().split()]

cop = sorted(set(List))

dic = {}

for i in range(len(cop)):
    dic[cop[i]] = i

for i in List:
    print(dic[i], end=' ')
