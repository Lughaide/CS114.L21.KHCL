n = list(map(int, input().split()))
Arr1 = list(map(int, input().split()))
Arr2 = list(map(int, input().split()))
i = 0
j = 0
k = 0
Arr3 = [None] * (n[0] + n[1])

while (i < n[0]) & (j < n[1]):
    if Arr1[i] < Arr2[j]:
        Arr3[k] = Arr1[i]
        i += 1
        k += 1
    else:
        Arr3[k] = Arr2[j]
        j += 1
        k += 1

while i < n[0]:
    Arr3[k] = Arr1[i]
    i += 1
    k += 1

while j < n[1]:
    Arr3[k] = Arr2[j]
    j += 1
    k += 1


print(*Arr3)
