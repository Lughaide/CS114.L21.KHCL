#Source: https://leetcode.com/problems/reshape-the-matrix/discuss/449268/python-with-and-without-numpy

n, m = list(map(int, input().split()))
r, c = list(map(int, input().split()))
datas = [list(map(int, input().split())) for i in range(n)]


if r * c == n * m:
    data = []
    #data = [nb for row in datas for nb in row]
    for row in datas:
        for nb in row:
            data.append(nb)
    pack = []
    #pack = [[data[c * i + j] for j in range(c)] for i in range(len(data) // c)]
    for j in range(r):
        pack.append([])
        for i in range(len(data) // r):
            pack[j].append(data[c * j + i])
    #But why was this value different?
    for i in range(r):
        print(*pack[i])
else:
    for i in range(n):
        print(*datas[i])


