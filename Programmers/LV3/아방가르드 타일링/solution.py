def solution(n):
    answer = 0
    # 가능한 데코 종류 [1,0(뒤의 작업에서 수행),1]  3의 배수마다 [2:2,3:4]
    dp = [1, 1, 3]
    twi = [0, 0, 1]
    ti = [0, 0, 0]
    fi = [0, 0, 0]
    for i in range(3, n+1):
        dp.append(dp[i-1]*1+dp[i-3]*1)
        # 기역자 블록 사이 가로 블럭 채우기
        twi[i % 3] += dp[i-2]
        dp[i] += twi[i % 3]*2
        ti[i % 3] += dp[i-3]
        dp[i] += ti[i % 3]*4
        if i > 3:
            fi[i % 3] += dp[i-4]
            dp[i] += fi[i % 3]*2

    answer = dp[n] % 1000000007
    return answer
