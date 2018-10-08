# def sqrtOf(value):
#     if not isinstance(value,(int,float)):
#         raise ValueError("Must be a Number")
#     if value<0:
#         raise TypeError("negative")
#     else:
#         return value*value
#
# def sout(value):
#     print(value)
# try:
#     print(4/0)
# except Exception:
#     print("zero divizion")
# #
# # sout(sqrtOf(5))
#
#
#
# def is_multiple(n, m):
#     result = str(n / m)
#     answer = False
#     if result[-1] == "0" and result[-2] == ".":
#         answer = True
#     return answer
#
#
# def isEven(k):
#     a = 0
#     for i in range(k):
#         a = a + 2
#         if (a == k):
#             return True
#     return False
#
#
# def pattern(scale):
#     result = []
#     counter = 0
#     result.append(counter)
#     for i in range(2, scale):
#         if i % 2 == 0:
#             counter += i
#             result.append(counter)
#
#     return result
#
#
# print(pattern(21))
# class point:
#     def __init__(self,x,y):
#         self.__x = x
#         self.__y = y
#     def __add__(self, other):
#         x = self.__x+other.getX()
#         y = self.__y+other.getY()
#         sumOfPoint = point(x,y)
#         return sumOfPoint
#     def getX(self):
#         return self.__x
#     def getY(self):
#         return self.__y
#     def __str__(self):
#         return "({},{})".format(self.__x,self.__y)
#
# p1 = point(1,2)
# p2 = point(1,2)
# print(p1+p2)

from abc import ABCMeta, abstractmethod
#
#
# class Human:
#     __name = ""
#     __age = 0
#     __sex = ""
#     __color = ""
#
#     def __init__(self, sex, color):
#         self.__sex = sex
#         self.__color = color
#
#     def getAge(self):
#         return self.__age
#
#     def setAge(self, age):
#         if isinstance(age, (int)) and age > 0:
#             self.__age = age
#         else:
#             raise Exception("Invalid age")
#
#     def getName(self):
#         return self.__name
#
#     def setName(self, name):
#         self.__name = name
#
#     def getSex(self):
#         return self.__sex
#
#     def getColor(self):
#         return self.__color
#
#     def __str__(self):
#         return " Age:{} \n Name:{} \n color:{}\n sex:{}".format(self.__age, self.__name, self.__color, self.__sex)
#
#
# zackariah = Human("M", "Black")
# zackariah.setName("zackariah")
# zackariah.setAge(19)
# # print(zackariah)
#
# def facto(n):
#     if n==1:
#         return 1
#     else:
#         return n*facto(n-1)
#
# def fibo(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 2
#     else:
#         return fibo(n-2)+fibo(n-1)
#
# def fibo2(n):
#     prevl = [1]
#     nextl = [2]
#     if n>2:
#         for i in range(2,n):
#             prevl[0] = prevl[0]+nextl[0]
#             nextl[0] = prevl[0]+nextl[0]
#     return nextl[0]
#
# print(facto(5))
# # print(fibo2(10))
#
# def drawPattern(n):
#     line = ""
#     for i in range(n):
#         line+="-"
#     return line
#
# def drawPatternforList(n):
#     line = ""
#     for i in n:
#         printer(drawPattern(i))
#
# def main(n):
#     for i in range(n):
#         printer(drawPattern(3),i)
#         drawPatternforList([1,2,1,3,1,2,1])
# def printer(value,n=""):
#     print(value+" "+str(n))
# main(10)
# from time import time
# def binarySearch(Array,value):
#     low = Array[0]
#     high = Array[-1]
#     if value==low:
#         return 0
#     if value==high:
#         return len(Array)-1
#     mid = len(Array)//2
#     while Array[mid]!=value:
#         if Array[mid]>value:
#             high = mid
#         else:
#             low = mid
#         mid = (low+high)//2
#     return mid
# timez = time()
# print(binarySearch([1,2,3,4,5,6,7],5))
# print(time()-timez)
import math as Math


def calculateStringHash(String, a):
    n = len(String)
    result = 0
    for i in range(len(String)):
        result += ord(String[i]) * Math.pow(a, n - i)

    print(result)


calculateStringHash('hh', 20)

# 41746817200.
