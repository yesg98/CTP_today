N = int(input())
dp = []
for i in range(N):
    if len(dp) == 0:
        dp.append([int(x) for x in input().split()])
    else:
        a, b, c = map(int, input().split())
        dp.append([a+min(dp[i-1][1], dp[i-1][2]), b+min(dp[i-1]
                  [0], dp[i-1][2]), c+min(dp[i-1][0], dp[i-1][1])])
print(min(dp[N-1]))
