import math

n = int(input())
for i in range (0, n):
    a = list(map(int, input().split()))
    tmp = math.gcd(a[0],a[1])
    b = a[0] // tmp
    c = a[1] // tmp
    if (c != 1):
        print(b, c)
    else:
        print(b)