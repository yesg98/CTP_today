# 테케 수 입력
T = int(input())

# 테스트
for _ in range(T):

    # 명령 입력
    com = list(input())

    # 숫자 수 입력
    N = int(input())

    # 숫자 입력
    List = input().strip('[').strip(']').split(',')

    # error 필터
    if com.count('D') > N:
        print("error")
        continue

    # len이 0일때
    if N == 0 or com.count('D') == N:
        print("[]")
        continue

    # 명령수행
    rev = True
    for i in com:
        if i == "R":
            rev = not rev
        if i == "D":
            if rev:
                List.pop(0)
            else:
                List.pop()

    # 출력
    if rev:
        res = '['
        for i in List:
            res += i+','
        res = res.rstrip(',')
        res += ']'
        print(res)

    else:
        List.reverse()
        res = '['
        for i in List:
            res += i+','
        res = res.strip(',')
        res += ']'
        print(res)
