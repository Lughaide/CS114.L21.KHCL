#Thanks to khiemledev for the brilliant matrix idea
h, w = map(int, input().split())
data = [list(map(int, input().split())) for i in range(h)]
top, left, bottom, right = map(int, input().split())
for i in range(h):
    if (i < top) | (i > bottom):
        data[i] = [0] * w
    data[i][:left] = [0] * left
    data[i][right+1:] = [0] * (w - right - 1)
for i in range(h):
    print(*data[i])