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







