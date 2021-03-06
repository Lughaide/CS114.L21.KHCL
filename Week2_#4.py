#Algorithm learned from Waqar-107's source code: https://github.com/Waqar-107/Codeforces/blob/master/C-set/114C.Grammar%20Lessons.py
import sys

chain = input().split()
num = len(chain)
MarkingArr = [0] * num
Ext = ("lios", "liala", "etr", "etra", "initis", "inites")

#If there's only 1 word
if num == 1:
    if chain[0].endswith(Ext):
        print('YES')
        sys.exit()
    else:
        print('NO')
        sys.exit()

#If there's a whole sentence
for i in range(0, num):
    #Mark using an array to define word type: adj -> noun -> vrb
    for j in range(0, len(Ext)):
        if chain[i].endswith(Ext[j]):
            MarkingArr[i] = j + 1
            break

    if MarkingArr[i] == 0:
        print('NO')
        sys.exit()

#Check the gender at the beginning of the sentence
Gender = MarkingArr[0] % 2
for i in range(0, num):
    if MarkingArr[i] % 2 != Gender:
        print('NO')
        sys.exit()

#Check the order of word type in the given sentence
Order = sorted(MarkingArr)
Repeated = 0 #Adding an extra variable to check if there are more than 1 noun
for i in range(0, len(MarkingArr)):
    if MarkingArr[i] != Order[i]:
        print('NO')
        sys.exit()

for i in range(num):
    if chain[i].endswith('etr') | chain[i].endswith('etra'):
        Repeated += 1
#Checking for number of nouns
if Repeated == 1:
    print('YES')
else:
    print('NO')