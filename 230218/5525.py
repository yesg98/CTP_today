# N 입력
N = int(input())

# 문자열 길이 입력
leng = int(input())

# 문자열 입력
stri = input()

# Pi 문자열 생성
p = "I"
for _ in range(N):
    p += "OI"

# 문자열 횟수 검사
n = 0
ind = 0
while True:
    ind = stri.find(p, ind)
    if ind == -1 or leng-ind < 2*N-1:
        break
    else:
        ind += 1
        n += 1

# 값 출력
print(n)
