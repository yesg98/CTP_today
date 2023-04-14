n = int(input())

dp = [5]*(n+1)
dp[0] = 0

for i in range(n+1):
    for j in range(1, (int(i**(1/2))+1)):
        dp[i] = min(dp[i], dp[i-j**2]+1)
print(dp[n])
