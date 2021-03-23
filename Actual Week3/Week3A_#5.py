from sys import stdin

new_arr = []
r, c = stdin.readline().split()
col = [1] * int(c)
for i in range(int(r)):
    new_arr.append([])
    new_arr[i] = list(map(int, stdin.readline().split()))
    for j in range(int(c)):
        if col[j] < len(str(new_arr[i][j])):
            col[j] = len(str(new_arr[i][j]))

#Goddamn integers man
for i in range(int(r)):
    for j in range(int(c)):
        new_arr[i][j] = str(new_arr[i][j]).rjust(col[j])
    print(*new_arr[i])
