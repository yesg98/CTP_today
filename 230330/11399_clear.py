N = int(input())
time = [int(x) for x in input().split()]

time.sort()
sum_time = 0

for i in range(N):
    sum_time += time[i]*(N-i)

print(sum_time)
