a, b, c = map(int, input().split())
d = 1
while b > 0:
    d *= a**(b % 2)
    d %= c
    b = b//2
    a = (a % c)*(a % c) % c
print(d)
