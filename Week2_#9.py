n = int(input())
for i in range(0, n):
    x = int(input())
    if x < 3:
        print(4 - x)
    else:
        Left = x // 2
        Right = x - Left
        print(Right - Left)