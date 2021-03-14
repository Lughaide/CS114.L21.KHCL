from heapq import nsmallest
n = int(input())
a = list(map(int, input().split()))
arr = list(map(int, input().split()))
x = nsmallest(arr[0], a, key=lambda x: abs(x - arr[1]))
x = sorted(x)
print(*x)
