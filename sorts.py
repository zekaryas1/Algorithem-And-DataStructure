# ----------------SELECTION SORT-----------------------
# def SortWithSelection(array):
#     last = len(array)
#     for i in range(0, last):
#         minimum = findMin(array, i, last)
#         indexMin = array.index(minimum)
#         array[i], array[indexMin] = array[indexMin], array[i]
#     return array
#
#
# def findMin(array, intial, last):
#     minimum = array[intial]
#     for i in range(intial, last):
#         if array[i] < minimum:
#             minimum = array[i]
#     return minimum
#
#
# print(SortWithSelection([7, 6, 5, 4, 3, 2, 1]))

# -----------------------INSERTION SORT-------------------

# def SortWithInsertion(array):
#     for i in range(1, len(array)):
#         j = i
#         # THIS IS WORKING BCOZ INSERTION WORKS BY SHIFTING TO THE LEFT <-----
#         while j > 0 and array[j - 1] > array[j]:
#             array[j - 1], array[j] = array[j], array[j - 1]
#             j = j - 1
#     return array
#
# print(SortWithInsertion([7, 6, 5, 4, 3, 2, 1]))

# -------------------------BUBBLE SORT--------------------

# def bubbleSort(array):
#     for j in range(len(array)):
#         for i in range(1,len(array)):
#             if array[i]<array[i-1]:
#                 array[i],array[i-1]=array[i-1],array[i]
#     return array
#
#
# print(bubbleSort([7,7, 6, 5, 4, 3, 2, 1]))


# --------------------------MERGE SORT---------------------
# import ctypes
#
#
# def mergeSort(theSeq):
#     n = len(theSeq)
#     tmpArray = theSeq.copy()
#
#     recMergeSort(theSeq, 0, n - 1, tmpArray)
#
#     print(theSeq)
#
#
# def mergeVirtualSeq(theSeq, left, right, end, tmpArray):
#     a = left
#     b = right
#     m = 0
#
#     while a < right and b < end:
#         if theSeq[a] < theSeq[b]:
#             tmpArray[m] = theSeq[a]
#             a += 1
#         else:
#             tmpArray[m] = theSeq[b]
#             b += 1
#         m += 1
#
#     while a < right:
#         tmpArray[m] = theSeq[a]
#         a += 1
#         m += 1
#     while b < end:
#         tmpArray[m] = theSeq[b]
#         b += 1
#         m += 1
#     for i in range(end - left):
#         theSeq[i + left] = tmpArray[i]
#
#
# def recMergeSort(theSeq, first, last, tmpArray):
#     if first == last:
#         return;
#     else:
#         mid = (first + last) // 2
#
#         recMergeSort(theSeq, first, mid, tmpArray)
#         recMergeSort(theSeq, mid + 1, last, tmpArray)
#
#         mergeVirtualSeq(theSeq, first, mid + 1, last + 1, tmpArray)
#
#
# if __name__ == '__main__':
#     mergeSort([8, 7, 6, 5, 4, 3, 2, 1])
# --------------------------QUICK SORT---------------------
# def quickSort(Array):
#     divide(Array)
#     print(Array)
#
#
# def divide(Array):
#     if len(Array) <= 1:
#         return
#     else:
#         pivote = Array[0]
#         left = []
#         right = []
#         for elt in Array:
#             if elt == pivote:
#                 continue
#             elif elt > pivote:
#                 right.append(elt)
#             elif elt < pivote:
#                 left.append(elt)
#         divide(left)
#         divide(right)
#         concure(Array, left, pivote, right)
#
#
# def concure(Array, left, pivote, right):
#     j = 0
#     for i in range(len(left)):
#         Array[i] = left[i]
#         j += 1
#
#     Array[j] = pivote
#     j += 1
#     for elt in right:
#         Array[j] = elt
#         j += 1

# --------------------------RADIX SORT---------------------

from ListQueue import Queue


def radixSort(Array):
    numdigit = len(numDigit(Array))

    holder = []
    for i in range(10):
        holder.append(Queue())
    column = 1

    for i in range(numdigit):
        for key in Array:
            place = (key // column) % 10
            holder[place].enqueue(key)

        i = 0
        for bin in holder:
            while not bin.isEmpty():
                Array[i] = bin.dequeue()
                i += 1

        column *= 10
    print(Array)


def numDigit(Array):
    return str(max(Array))


if __name__ == '__main__':
    radixSort([10, 23, 51, 18, 4, 31, 5, 13])
