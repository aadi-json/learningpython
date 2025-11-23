'''

Day:2

using normal for loop
----------------------

# for loop :
# set of instruction that executes again and again
#  when we know the num of itreation

syntax:1
for refreance variable in iterable:
    statements

syntax:2
for refreance variable in iterable:
    statements

1. 

a=[1,2,3]
for i in a:
    print(i) ---------> col format output
    print(i,end='')------------> one line output format

2.
a=[1,2,3]
for i in a:
    print(i,end=',')-------> here ',' is saperator

3.

a={1:2,3:4,5:6,7:8}
for i in a.values():
    print(i,end=" ")

4.
    
a={1:2,3:4,5:6,7:8}
for i in a:
    print(a[i],end=" ") 

5.
a={1:2,3:4,5:6,7:8}
for i in a:
    print(i,a[i],end=" ")

6.
d=[10,20,30,40,50,51]
for i in d:
    if i%2==0:
        print(i)

7.
        
d=[10,20,30,40,50,51]
for i in d:
    if i%2==1:
        print(i)

8.

e=['Python','java','hello','walmart']
for i in e:
    if len(i)%2==0:
        print(i)

9.

e=['Python','java','hello','walmart']
for i in e:
    if len(i)%2==0:
        print(i)
    else:
        print(i[::-1])

10.
d="hello"
d1={}
for i in d:
    d1[i]=ord(i)

print(d1)

11.
d="hello"
d1={}
for i in d:
    d1.update({i:ord(i)})
print(d1)

12.

lst=[100,200,300,1000]
lst1=[]
for i in lst:
    lst1=[i]+lst
print(lst1)


13.
lst='good luck'
lst1=""
for i in lst:
    lst1=i+lst1
print(lst1)

14.
s=[1,'hii',True,[1,2],(1,2),{1,2},{9:0,6:8}]
for i in s:
    if type(i) in [int,bool,complex,float]:
        print(i)

15.
s=[1,'hii',True,[1,2],(1,2),{1,2},{9:0,6:8}]
for i in s:
    if type(i) in [str,tuple,list,dict]:
        print(i)

16.
w="think"
d=0
for i in w:
    d=d+1
print(d)

-------------------------------------------------------------------------------

Day:2 using range
------------------

syntax 2: 
for reference_variable in range(start,end,step):
    statement

1.to print first 10 numbers
for i in range(1,11,1):
    print(i,end=",")

2.to prints even number upto 10
for i in range(2,11,2):
    print(i,end=",")

another way
-------------
for i in range(1,11,2):
    print(i+1,end=",")

3.to print odd numbers

for i in range(1,11):
    if i%2==1:
        print(i,end=",")

4.
for i in range(1,16):
    print(i,end=",")

5.to print even and odd saperately

evan=[]
odd=[]

for i in range(101,200):
    if i%2==0:
        evan.append(i)
    else:
        odd.append(i)
print(evan)
print(odd)

6. to print index plus char saperately

k='camlin'
for i in range(0,len(k)):
    print(i,k[i])

another one
--------------

s=[10,78.90,'map','pen','look']
for i in range(0,len(s)):
    print(i,s[i])

# enamurate
------------
only accept only one iterble
return type is tuple
to unpack there are two ways using * or take 2 variables

syntax----------> enumarate(iterable)

a="java"
print(list(enumerate(a)))

op:- [(0, 'j'), (1, 'a'), (2, 'v'), (3, 'a')]

Note: if we want to print sequence of character without using range() function

in unpacked format
------------------

a="python"
for i in enumerate(a):
    print(*i)

reversing ways :-
------------------

reversed(iterable):
--------------------
a="aditya"
for i in reversed(a):
    print(i,end="")

b=[1,2,3]
for i in reversed(b):
    print(i,end="")

Note: use it on list dont use it other iterables

using tuple
-------------
a=(10,20,30,50,'PYTHON')
for i in reversed(a):
    print(i,end=" ")

a='python'
for i in a[::-1]:
    print(i,end=" ")

a='python'
for i in range(-1,-len(a),-1):
    print(i,a[i])

a="python"
b=''
for i in a:
    b=i+b
print(b)

#zip():
---------
we can pass unlimited iterable there is one condition the length of the iterable must be same otherwise there will be a data loss
return type is tuple


a=[1,2,3]
b=[4,5,6]
print(zip(a,b))-------------> object address  to avoid this use loop or typecasting

1.typecasting:
a=[1,2,3]
b=[4,5,6]
print(zip(a,b))
print(list(zip(a,b)))

2.looping

a=[1,2,3]
b=[4,5,6]
for i in zip(a,b):
    print(i)

zip-longest():- 
->to avoid data loss we use zip-longest
-> we cant directly work on zip-longest we have to import it

from itertools import zip_longest

with type casting
------------------

s='python'
c=(1,2)
print(list(zip_longest(s,c)))

using loop
------------

s='python'
c=(1,2)
for i in zip_longest(s,c,fillvalue="new"):
    print(i)

Note:- if the value is not present it will show none to avoid none we use fillvalue property
    
'''





































