#Python Programming Assignement 
#Q1. Find the Largest Element in an Array
#Example:
#- Input: "[10, 25, 8, 45, 32, 15]"
#- Output: "45"
a=[10, 25, 8, 45, 32, 15]
l=-100000000
for each in a:
    if(each>l):
        l=each
print(l)
#Q2. Count Frequency of Each Element in an Array
#Example:
#- Input: "[1, 2, 2, 3, 1, 4, 2, 3]"
#- Output:
#  - 1 occurs 2 times
#  - 2 occurs 3 times
#  - 3 occurs 2 times
#  - 4 occurs 1 times
a=[1, 2, 2, 3, 1, 4, 2, 3]
d={}
for each in a:
    if(each in d):
        d[each]+=1
    else:
        d[each]=1
for keys,values in d.items():
    print(keys,"occurs",values,"times")
#Q3. Check if a Number is Prime
#Example:
#- Input: "7"
#- Output: "Prime Number"
n=int(input("enter the number:"))
is_prime=True
if(n<=1):
    is_prime=False
else:
    for i in range(2,(n//2)+1):
        if(n%i==0):
            is_prime=False
if(is_prime):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
#Q4. Find Factorial of a Number (Iterative)
#Example:
#- Input: "5"
#- Output: "120"
def fact(n):
    if(n==1):
        return 1
    return n*fact(n-1)
print(fact(5))
#Q5. Reverse an Integer
#Example:
#- Input: "12345"
#- Output: "54321"
n=int(input("enter the number:"))
rev=0
while(n>0):
    last_d=n%10
    rev=rev*10+last_d
    n=n//10
print(rev)
#Q6. Find GCD (HCF) of Two Numbers
#Example:
#- Input: "12, 18"
#- Output: "6"
n1=12
n2=18
for i in range(12,0,-1):
    if(n1%i==0 and n2%i==0):
        print(i)
        break
#Q7. Check if a String Contains Only Digits
#Example:
#- Input: ""123456""
#- Output: "True"
n="123456"
print(n.isdigit())
#Q8. Find the Average of Array Elements
#Example:
#- Input: "[4, 8, 15, 16, 23, 42]"
#- Output: "18.0"
a=[4, 8, 15, 16, 23, 42]
n=len(a)
sum=0
for each in a:
    sum+=each
print(sum/n)
#Q9. Convert a String to Uppercase Manually
#Example:
#- Input: ""infosys""
#- Output: ""INFOSYS""
#1st approach
s="infosys"
u=""
for ch in s:
    b=ch.upper()
    u+=b
print(u)
#2nd approach
s="infosys"
u=""
for ch in s:
    if(ch>="a" and ch<="z"):
        u+=chr(ord(ch)-32)
print(u)

#Q10. Find the Union of Two Arrays
#Example:
#- Input: "arr1 = [1, 2, 3]", "arr2 = [2, 3, 4]"
#- Output: "[1, 2, 3, 4]"
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
a=set(arr1)
b=set(arr2)
print(list(a.union(b)))
#2nd approach
arr1=[1,2,3]
arr2=[2,3,4]
d={}
union=[]
for num in arr1:
    if(num in d):
        d[num]+=1
    else:
        d[num]=1
for num in arr2:
    if(num in d):
        d[num]+=1
    else:
        d[num]=1
for keys in d.keys():
     union.append(keys)
print(union)
#3rd approach
arr1=[1,2,3]
arr2=[2,3,4]
union=[]
for num in arr1:
    if(num not in union):
        union.append(num)
    for num in arr2:
        if(num not in union):
           union.append(num)
print(union)