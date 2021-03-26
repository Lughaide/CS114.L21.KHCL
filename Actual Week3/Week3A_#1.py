#Source + idea: https://github.com/ttknguyen/CS114.L22.KHCL/blob/master/Assignment/19520188/Week3-DataStructures/problem1.py
from sys import stdin, stdout
from bisect import bisect_left

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

while True:
    val = list(map(int, stdin.readline().split()))
    if len(val) == 0:
        break
    if val[1] > arr[-1]:
        stdout.write(str(arr[-val[0]]) + ' ')
        stdout.write(str(arr[-1]) + '\n')
    elif val[1] < arr[0]:
        stdout.write(str(arr[0]) + ' ')
        stdout.write(str(arr[val[0] - 1]) + '\n')
    else:
        pos = bisect_left(arr, val[1])
        i, j = pos, pos + 1
        for y in range(val[0]):
            if i < 0:
                i, j = -1, val[0]
                break
            if j == len(arr):
                i, j = -val[0]-1, 0
                break
            if val[1] - arr[i] <= arr[j] - val[1]:
                i -= 1
            else:
                j += 1
        stdout.write(str(arr[i + 1]) + ' ')
        stdout.write(str(arr[j - 1]) + '\n')
