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
