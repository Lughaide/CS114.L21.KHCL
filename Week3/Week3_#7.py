from sys import stdout, stdin
new_db = {}
while 1:
    #Input#
    a = stdin.readline().split()
    if len(a) == 0:
        quit(0)
    #Checking values#
    if a[0] == '0':
        quit(0)
    if a[0] == '1':
        new_db[a[1]] = 1
    elif a[0] == '2':
        if a[1] in new_db:
            stdout.write('1\n')
        else:
            stdout.write('0\n')
    else:
        new_db.pop(a[1], None)