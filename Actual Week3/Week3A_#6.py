from sys import stdin, stdout
import collections
q = int(stdin.readline())

for i in range(q):
    n, k = stdin.readline().split()
    new_d = stdin.readline().split()
    cnt = collections.Counter(new_d)
    stdout.write(str(cnt[k]) + '\n')
