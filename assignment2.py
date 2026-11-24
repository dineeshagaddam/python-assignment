#find the second smallest element in the array
#given an array of distinct integers find the second smallest element in a single pass
#input=[12,13,1,10,34]
#output:10
a=[12,13,1,10,34]
f_s=a[0]
s_s=a[0]
for i in a:
   if(i<f_s):
       f_s=i
       s_s=a[0]
   elif(i<s_s):
       s_s=i
print(s_s)


#find majority element 
#given an array of size N find the element that appears more than n/2 times assume it always exists
#input=[2,2,1,1,1,2,2]
#output:2
a=[2,2,1,1,1,2,2]
dict={}
n=len(a)//2
for i in a:
    if(i in dict):
        dict[i]+=1
    else:
        dict[i]=1
for keys,values in dict.items():
    if(values>n):
        print(keys)
#rearrange array in alternating positive and negative order
#given an array with positive and negative numbers rearrange it so that positive and negative numbers appears alternatively starting with
#positive number preserve the relative order within each sign as much as possible
#input=[1,2,-3,-1,4,-5]
#output:[1,-3,2,-1,4,-5]
a=[1,2,-3,-1,4,-5]
pos=[]
neg=[]
for i in a:
    if(i>0):
        pos.append(i)
    else:
        neg.append(i)
result=[]
for k in range(len(pos)):
    result.append(pos[k])
    result.append(neg[k])
print(result)
# find a peak element in an array
# a peak element is one of that is strictly greater thean its neighbours find the index of any peak element using 0(logN) time
#input=[1,2,3,1]
#output=2(index of elemnt 3)
a=[1,2,3,1]
for i in range(len(a)):
    if i==0:
        if(a[i]>a[i+1]):
            print(i)
    elif i==len(a)-1:
        if(a[i]>a[i-1]):
            print(i)
    elif a[i]>a[i+1] and a[i]>a[i-1]:
        print(i)
#binary search
l=0
r=len(a)-1
while(l<r):
    mid=(l+r)//2
    if(a[mid]>a[mid+1]):
        r=mid
    else:
        l=mid+1
print(l,a[l])
#count no of set bits in an integer 
#given an non negative integer count the number of 1s in its binary representation
#input=29
#output=4
n=int(input("enter the number"))
count=0
while n>0:
  r=n%2
  if r==1:
      count+=1
  n=n//2
print(count)
#chech whwather number is an armstrong
#input=153
#output=True
n=int(input("enter the number:"))
temp=n
pw=len(str(n))
sum=0
while(n>0):
    last_d=n%10
    sum+=last_d**pw
    n=n//10
if(temp==sum):
    print("True")
else:
    print("false")
#sum of array elements using recursion
#given an array of integers calculate  the sum of all elments using a recursive function without using loops
#input=[1,2,3,4,5]
#output=15
ar=[1,2,3,4,5]
def sums(ar,n):
    if n==0:
        return 0
    return ar[n-1]+sums(ar,n-1)
ar=[1,2,3,4,5]
print(sums(ar,len(ar)))
#find the longest word in a sentence
#given a sentence find the longest word if multiple words have the same max length return the first one encountered
#input="infosys hires specialist programmers"
#output="programmers"
s="infosys hires specialist  programmers "
b=s.split(" ")
l=[]
for each in b:
    lent=len(each)
    l.append(lent)
maxi=max(l)
for each in b:
    if(maxi==len(each)):
        print(each)
        break