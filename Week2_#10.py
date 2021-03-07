q = int(input())
for i in range (0, q):
    a = list(input())
    b = list(input())
    Sum = 0
    for j in range(0, len(a)):
        for l in range(0, len(b)):
            if a[j] == b[l]:
                Sum += 1
    if Sum == 0:
        print('NO')
    else:
        print('YES')