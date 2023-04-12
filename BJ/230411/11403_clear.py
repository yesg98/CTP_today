N = int(input())

road = []
for i in range(N):
    road.append([int(x) for x in input().split()])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if road[i][k]+road[k][j] == 2:
                road[i][j] = 1

for i in road:
    for j in i:
        print(j, end=' ')
    print()
