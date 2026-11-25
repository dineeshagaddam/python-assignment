#Q1. Reverse a String Problem Statement:
#Given a string, reverse the string without using any inbuilt string reversing methods.
#Examples:#Input: "hello" → Output: "olleh"
#Input: "python" → Output: "nohtyp"
#Input: "12345" → Output: "54321" 
s=input("enter the strig:")
rev=''
for ch in s:
    rev=ch+rev
print(rev)
# Q2. Check Whether a String Is a Palindrome Problem Statement:
#Given a string, check whether it is a palindrome or not. A string is called a palindrome if it reads the same forward and backward.
#Examples:
#Input: "madam" → Output: Palindrome
#Input: "level" → Output: Palindrome
#Input: "hello" → Output: Not a Palindrome
#Input: "121" → Output: Palindrome
s=input("enter the string:")
rev=""
for ch in s:
    rev=ch+rev
if rev==s:
    print("palindrome")
else:
    print("not a palindrome"
#  Q3. Count Vowels and Consonants in a String Problem Statement:
#Given a string, count the number of vowels and consonants present in it.
#Vowels: a, e, i, o, u
#Examples:
#Input: "hello" → Output: Vowels = 2, Consonants = 3
#Input: "python" → Output: Vowels = 1, Consonants = 5
#Input: "education" → Output: Vowels = 5, Consonants = 4 
# Note: Do not use inbuilt string methods. Ignore spaces, digits, and special characters.
s=input("enter the string")
v=['a','A','e','E','i','I','o','O','u','U']
vowels=0
consonants=0
for ch in s:
    if(ch  in v):
        vowels+=1
    elif ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        consonants+=1
print(vowels)
print(consonants)
#find difference between largest and smallest element
a=[10,5,25,8,15]
l=a[0]
s=a[0]
for i in a:
    if(i>l):
        l=i
    elif(i<s):
        s=i
print(l-s)
#move all zeros to end
a=[1,0,8,0,9,4,0]
l=0
r=0
for i in range(len(a)):
    if(a[r]!=0):
        a[l],a[r]=a[r],a[l]
        l+=1
        r+=1
    else:
        r+=1
print(a)
# 2nd approach 
a=[1,0,8,0,9,4,0]
l=[]
count=0
for i in a:
    if(i!=0):
        l.append(i)
    else:
        count+=1
for i in range(count):
    l.append(0)
print(l)
