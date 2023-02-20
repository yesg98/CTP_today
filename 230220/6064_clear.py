# 테스트 케이스 개수
T = int(input())

# 테스트 수행
for _ in range(T):
    M, N, x, y = map(int, input().split())
    if N == y:
        y = 0
    res = 0
    n = x
    fsty = x % N
    while True:
        if n % N == y:
            res = n
            break
        n += M
        if n % N == fsty:
            break

# 결과 출력
    if res:
        print(res)
    else:
        print(-1)
