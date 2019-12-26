def quickSort(Array):
    divide(Array)
    print(Array)


def divide(Array):
    if len(Array) <= 1:
        return
    else:
        pivote = Array[0]
        left = []
        right = []
        for elt in Array:
            if elt == pivote:
                continue
            elif elt > pivote:
                right.append(elt)
            elif elt < pivote:
                left.append(elt)
        divide(left)
        divide(right)
        concure(Array, left, pivote, right)


def concure(Array, left, pivote, right):
    j = 0
    for i in range(len(left)):
        Array[i] = left[i]
        j += 1

    Array[j] = pivote
    j += 1
    for elt in right:
        Array[j] = elt
        j += 1
