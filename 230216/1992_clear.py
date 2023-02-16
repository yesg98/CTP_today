def divq(a, b):
    # 데이터가 한개면 바로 값 리턴
    if b == 1:
        return a[0][0]

    # 데이터가 여러 개면 모든 데이터가 같은 값인지 확인
    sta = True
    for i in a:
        for j in i:
            if j != a[0][0]:
                sta = False
                break
        if not sta:
            break

    # 데이터가 모두 같으면 압축해서 값 리턴
    if sta:
        return a[0][0]

    # 데이터가 다르면 재귀함수 호출
    res = '('
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    aup = a[:len(a)//2]
    for i in aup:
        a1.append(i[:len(i)//2])
        a2.append(i[len(i)//2:])
    adw = a[len(a)//2:]
    for i in adw:
        a3.append(i[:len(i)//2])
        a4.append(i[len(i)//2:])

    res += divq(a1, b//2)
    res += divq(a2, b//2)
    res += divq(a3, b//2)
    res += divq(a4, b//2)
    res += ')'
    return res


# 영상크기 입력
N = int(input())

# 영상 입력받기
List = [list(input()) for _ in range(N)]

print(divq(List, N))
