# 테스트케이스 입력
T = int(input())

dp = [[1, 0, 0], [1, 1, 0], [2, 1, 1]]

# 테스트 수행
for _ in range(T):
    n = int(input())
    for i in range(len(dp), n):
        dp.append([sum(dp[i-1]), dp[i-1][0], dp[i-1][1]])
    print(sum(dp[n-1]))
