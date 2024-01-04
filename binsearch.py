def binsearch(L, x, lower, upper):
    mid = (lower + upper) // 2
    if lower > upper:
        print(lower, mid, upper)
        return -1
    print(lower, mid, upper)
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binsearch(L, x, lower, mid - 1)
    else:
        return binsearch(L, x, mid + 1, upper)

L = [1, 3, 7, 9, 13, 14, 16, 17, 19, 25, 33, 53, 79, 100, 123]
x = int(input("Target Number: "))
print(binsearch(L, x, 0, len(L) - 1))