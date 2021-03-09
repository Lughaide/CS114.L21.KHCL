x = list(map(int, input().split()))
m = x[0]
n = x[1]
a = x[2]
Length = 0
Width = 0
while m > 0:
    Length += 1
    m = m - a
while n > 0:
    Width += 1
    n = n - a
print (Length * Width)