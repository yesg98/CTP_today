T = int(input())

dp = [1, 1, 1, 2, 2]

for _ in range(T):
    N = int(input())
    for i in range(len(dp), N):
        dp.append(dp[i-1]+dp[i-5])
    print(dp[N-1])
