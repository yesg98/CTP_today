# 계단 개수 입력
N = int(input())

# 계단 점수 입력
score = [int(input()) for _ in range(N)]

# dp 배열 생성
dp = [[score[0], score[0]]]

# dp 알고리즘 수행
for i in range(1, N):
    if i == 1:
        dp.append([score[0]+score[1], score[1]])
    else:
        dp.append([dp[i-1][1]+score[i], max(dp[i-2])+score[i]])

print(max(dp[N-1]))
