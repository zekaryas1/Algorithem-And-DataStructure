import ctypes


def mergeSort(theSeq):
    n = len(theSeq)
    tmpArray = theSeq.copy()

    recMergeSort(theSeq, 0, n - 1, tmpArray)

    print(theSeq)


def mergeVirtualSeq(theSeq, left, right, end, tmpArray):
    a = left
    b = right
    m = 0

    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpArray[m] = theSeq[a]
            a += 1
        else:
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1

    while a < right:
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1
    while b < end:
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1
    for i in range(end - left):
        theSeq[i + left] = tmpArray[i]


def recMergeSort(theSeq, first, last, tmpArray):
    if first == last:
        return;
    else:
        mid = (first + last) // 2

        recMergeSort(theSeq, first, mid, tmpArray)
        recMergeSort(theSeq, mid + 1, last, tmpArray)

        mergeVirtualSeq(theSeq, first, mid + 1, last + 1, tmpArray)


if __name__ == '__main__':
    mergeSort([87, 7, 6, 5, 4, 3, 2, 41])
