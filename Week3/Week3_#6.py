import sys
new_db = {}
while 1:
    try:
        a, b = list(map(int, input().split()))
    except ValueError:
        quit(0)
    if a == 1:
        new_db[b] = b
    else:
        if b in new_db:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
