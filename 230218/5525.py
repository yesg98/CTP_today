# N 입력
N = int(input())

# 문자열 길이 입력
leng = int(input())

# 문자열 입력
stri = input()


# 문자열 횟수 검사
res = 0
n = 0
bef = 'I'
for i in stri:
    if i == 'I':
        if bef=='IO':
            n+=1
            bef = 'I'
        else:
            if n:
                if n>=N:
                    res += n-N+1
                n=0
            bef = 'I'
    else:
        if bef=='I':
            bef='IO'
        else:
            if n:
                if n>=N:
                    res+=n-N+1
                n=0
            bef = 'O'

# 값 출력
print(res)
