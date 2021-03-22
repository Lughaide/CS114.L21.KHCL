import math
from sys import stdin, stdout

n, m = stdin.readline().split()
sum = 0
length = int(math.pow(10, len(n)))
sum = (int(m) - int(n)) // length + 1
stdout.write(str(sum))