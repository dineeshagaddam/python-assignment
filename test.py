#Q1. Find the Largest Element in an Array Problem Statement:
#Given an array of integers, find and print the largest element without using the built-in max() function.
#Examples:
#Input: [10, 25, 8, 40, 15]
#Output: 40
#Input: [5, 12, 3, 9]
#Output: 12 
a=[5,12,3,9]
l=a[0]
for i in a:
    if(i>l):
        l=i
print(l)
#Q2. Print Fibonacci Series up to N Terms Problem Statement:
#Given an integer N, print the first N terms of the Fibonacci series.
#In the Fibonacci series, each number is the sum of the previous two numbers. Start with 0 and 1.
#Examples:
#Input: 7
#Output: 0 1 1 2 3 5 8
#Input: 5
#Output: 0 1 1 2 3 
n=int(input("enter number:"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b 
    a=b 
    b=c
#Q3. Find a Peak Element in an Array Problem Statement:
#Given an array of integers, find an element that is greater than or equal to its neighbouring elements.
#For the first and last elements, consider only the available neighbour.
#Examples:
#Input: [1, 3, 20, 4, 1, 0]
#Output: 20
#Input: [10, 5, 3, 2]
#Output: 10
#Input: [1, 2, 3, 4, 5]
#Output: 5 
a=[1,2,3,4,5]
for i in range(len(a)):
    if i==0:
        if(a[i]>a[i+1]):
            print(a[i])
    elif i==len(a)-1:
        if(a[i]>a[i-1]):
            print(a[i])
    elif a[i]>a[i+1] and a[i]>a[i-1]:
        print(a[i])
#Q4. Find the Missing Number in an Array Problem Statement:
#Given an array containing distinct numbers from 1 to N, with exactly one number missing, find the missing number.

#Examples:

#Input: [1, 2, 4, 5, 6]
#Output: 3
#Input: [2, 3, 1, 5]
#Output: 4
#Input: [1, 3, 4, 5]
#Output: 2
a=[1,3,4,5]
for i in range(1,len(a)+1):
    if(i not in a):
        print(i)