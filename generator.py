'''
GENERATOR:
------------------
-> The sequence of element it will generate one by one

DIFFERENCE B/W RETURN AND YIELD:
---------------------------------------------------
-> Return: 1.used in function 2.only execute one time
-> yeild : 1.used is generator 2.execute all time as meny time you mention

x=[1,2.1,3,True,False]

def op(x):
    for i in x:
        if isinstance(i,(float,bool)):
            yield i
w=op([1,2.1,3,True,False])
print(next(w))
print(next(w))
print(next(w))
print(next(w))------->StopIteration error due to print more element than present

close():
--------
->used to close the operation . if you again call next function after that it will throw StopIteration error

x=[1,2.1,3,True,False]

def op(x):
    for i in x:
        if isinstance(i,(float,bool)):
            yield i
w=op([1,2.1,3,True,False])
print(next(w))
w.close()
print(next(w))---------->StopIteration error

def demo():
    yield "A"
    yield "B"
    yield "C"
    yield "D"
w=demo()
# print(w)---------->generator object demo at 0x0000014201F16A40>
print(next(w))
# w.close()
print(next(w))
# w.close()
print(next(w))
w.close()
print(next(w))

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

if you use single yield then at a time you will get the op and return type is tuple

def demo():
    yield "A","B","C","D"
w=demo()
print(list(w))

op:-[('A', 'B', 'C', 'D')]

----------------------------------------------------------------------------------------------------------------------------------------------------------------

-->yield from is used to get the data from one function to another function

def first():
    yield "A"
    yield "B"

def second():
    yield "C"
    yield from first()
    yield "D"

c=second()

print(list(c))

in second() i used yield from first() which i can access by using c var
we don't have to create a separate object for first()

to avoid looping we use this method

def demo():
    yield from range(0)

def demo2():
    yield from range(10)

def demo3():
    yield from demo()
    yield from demo2()

w=demo3()
print(next(w))

'''
from pandas.io.sql import SQLTable
from pygments.styles.dracula import yellow


# wap to generate only the string with odd length in the
# given list

#function:
# def word():
#     words=["king","queen","jack","kohli","hero"]
#     for i in words:
#         if len(i)%2==1:
#             print(i)
# word()

# def word():
#     words=["king","queen","jack","kohli","hero"]
#     for i in words:
#         if len(i)%2==1:
#             yield i
# w=word()
# print(next(w))
# print(next(w))


# wap to generate only the numeric value in list

# def lst():
#     l=[1,2,3.1,'hii',True,False,[1,23]]
#     for i in l:
#         if isinstance(i,(int,float)):
#              print(i)
# lst()

# def lst():
#     l=[1,2,3.1,'hii',True,False,[1,23]]
#     for i in l:
#         if isinstance(i,(int,float)):
#              yield i
# c=lst()
# print(next(c))


# wap to generate a list if it is individual data type
# reverse it else keep it as it is

# def name():
# #     a = ["good", 45, [1, 2], 78.6, (4, 5), 8 + 7j, {9, 7}, False, {"a": 75}]
# #     for i in a:
# #         if isinstance(i, (float, bool,int,complex)):
# #             c=str(i)
# #             print(c[::-1])
# #         else:
# #             print(i)
# # name()

# def name():
#     a = ["good", 45, [1, 2], 78.6, (4, 5), 8 + 7j, {9, 7}, False, {"a": 75}]
#     for i in a:
#         if isinstance(i, (float, bool,int,complex)):
#             c=str(i)
#             yield c[::-1]
#         else:
#             yield i
# e=name()
# print(next(e))
# print(next(e))

# wap to return an iterator having the words and its length pair as a dictionary inside the tuple.

# def word():
#     l = ["charlie", "golden retriever", "scooby", "sandy", "german shepherd"]
#     d={}
#     for i in l:
#         d[i]=len(i)
#     print(d)
# word()

# def word():
#     l = ["charlie", "golden retriever", "scooby", "sandy", "german shepherd"]
#     d={}
#     for i in l:
#         d[i]=len(i)
#     yield d
# v=word()
# print(next(v))

# wap to generate a+b,a-b,a*b,a/b by taking a and b from user

# def op(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     return add,sub,mul,div
# c=op(10,20)
# print(c)

# def op(a,b):
#     add=a+b
#     sub=a-b
#     mul=a*b
#     div=a/b
#     yield add,sub,mul,div
# c=op(10,20)
# print(next(c))

# wap to return a iterator which is having square root of values present in the list

# def demp():
#     l = [25, 36, 49, 81, 16]
#     for i in l:
#         l2=[]
#         l2.append(i**0.5)
#         print(l2)
# demp()

# def demp():
#     l = [25, 36, 49, 81, 16]
#     for i in l:
#         l2=[]
#         l2.append(i**0.5)
#         yield l2
# c=demp()
# print(next(c))
# wap to return a iterator having tuples of word and its len pair and typecast into dictionary

# def demo():
#     l = ["instagram", "facebook", "whatsapp", "meta", "oracle"]
#     d={}
#     for i in l:
#         c=i,len(i)
#         d[c[0]]=c[1]
#     print(d)
# demo()

# def demo():
#     l = ["instagram", "facebook", "whatsapp", "meta", "oracle"]
#     for i in l:
#         d = {}
#         c=i,len(i)
#         d[c[0]]=c[1]
#     yield d
# w=demo()
# print(next(w))

# wap to generate only numeric values in given list

# def num():
#     l = ["flipkart", "Amazon", 78, [2, 3, 4], 78, 9.87, (5, 3), 45.36]
#     for i in l:
#         if isinstance(i,(float,int)):
#             print(i)
# num()

# def num():
#     l = ["flipkart", "Amazon", 78, [2, 3, 4], 78, 9.87, (5, 3), 45.36]
#     for i in l:
#         if isinstance(i,(float,int)):
#             print(i)
# num()

# def num():
#     l = ["flipkart", "Amazon", 78, [2, 3, 4], 78, 9.87, (5, 3), 45.36]
#     for i in l:
#         if isinstance(i,(float,int)):
#             yield i
# v=num()
# print(next(v))

# wap to generate a list if it is individual data type reverse it else return as it is
# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
# def demo():
#     l = ["flipkart", "Amazon", 78, [2, 3, 4], 78, 9.87, (5, 3), 45.36]
#     for i in l:
#         if isinstance(i,(int,float,bool,complex)):
#             c=str(i)
#             print(c[::-1])
#         else:
#             print(i)
# demo()

# l=["flipkart","Amazon",78,[2,3,4],78,9.87,(5,3),45.36]
# def demo():
#     l = ["flipkart", "Amazon", 78, [2, 3, 4], 78, 9.87, (5, 3), 45.36]
#     for i in l:
#         if isinstance(i,(int,float,bool,complex)):
#             c=str(i)
#             yield  c[::-1]
#         else:
#             yield i
# w=demo()
# print(next(w))

# wap to generate only the string with odd length in given list

# def rev():
#     l = ["alexa", "siri", "google", "cortrena"]
#     for i in l:
#         if len(i)%2==1:
#             print(i)
# rev()

# def rev():
#     l = ["alexa", "siri", "google", "cortrena"]
#     for i in l:
#         if len(i)%2==1:
#             yield i
# c=rev()
# print(next(c))

# wap to create a list of numbers if number are even square it else cube it

# def demo():
#     l = [2, 3, 4, 5, 6, 7]
#     for i in l:
#         if i%2==0:
#             print(i**2)
#         else:
#             print(i**3)
# demo()

# def demo():
#     l = [2, 3, 4, 5, 6, 7]
#     for i in l:
#         if i%2==0:
#             yield i**2
#         else:
#             yield i**3
# c=demo()
# print(next(c))

# wap to return a list if words is of even length reverse it

# def rev():
#     l = ["hello", "world", "python", "apple", "google", "walmart"]
#     for i in l:
#         if len(i)%2==0:
#             print(i)
# rev()


# def rev():
#     l = ["hello", "world", "python", "apple", "google", "walmart"]
#     for i in l:
#         if len(i)%2==0:
#             yield i
# c=rev()
# print(next(c))

# wap to generate the first letter of the word as key and words starting with letter as value
# def ge():
#     s = "python is a programming language and programming is part of life"
#     d = {}
#     for i in s.split():
#         if i[0] not in d:
#             d[i[0]] = [i]
#         else:
#             d[i[0]]+=[i]
#     print(d)
# ge()

# output:-->[{'p': ['python', 'programming', 'programming', 'part'], 'i': ['is', 'is'], 'a': ['a', 'and'], 'l': ['language', 'life'], 'o': ['of']}]

# wap to generate a list if it is individual data type
#reverse it else keep it as it is

# def demo():
#     a = ["good", 45, [1, 2], 78.6, (4, 5), 8 + 7j, {9, 7}, False, {"a": 75}]
#     for i in a:
#         if isinstance(i,(int, float, bool,complex)):
#             c=str(i)
#             print(c[::-1])
#         else:
#             print(i)
# demo()

# def demo():
#     a = ["good", 45, [1, 2], 78.6, (4, 5), 8 + 7j, {9, 7}, False, {"a": 75}]
#     for i in a:
#         if isinstance(i,(int, float, bool,complex)):
#             c=str(i)
#             yield c[::-1]
#         else:
#             yield i
# c=demo()
# print(next(c))

# 1.Generator to yield only vowels from a string
# a="well Played boys"
# def demo(a):
#     for i in a.split():
#         # print(i)
#         for j in i:
#             if j in "aeiou":
#                 yield j
# c=demo(a)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


# 2.Generator that yields word by word from a sentence
# b="I love Python"
# def demo(b):
#     for i in b.split():
#         yield i
# c=demo(b)
# print(next(c))
# print(next(c))
# print(next(c))

# 3.Generator that yields alternating even and odd
# o/p-->Odd:1 → Even:2 → Odd:3 → Even:4 → Odd:5

# def demo():
#     for i in range(1,11):
#         if i % 2 == 1:
#             yield "odd :",i
#         else:
#             yield "even :",i
# c=demo()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# 4.Generator to yield running sum
# x=[1,2,3,4,5]
# def s(x):
#     total = 0
#     for i in x:
#         total+=i
#         yield total
# c=s(x)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))



# 5.Generator to yield powers of 2

# def pow():
#     for i in range(1,10):
#         yield i**2
# c=pow()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# 6.Generator that yields only palindromes from a list

# def pal():
#     a=["hii","level","mom","dad","aditya"]
#     for i in a:
#         if i==i[::-1]:
#             yield i
# c=pal()
# print(next(c))
# print(next(c))
# print(next(c))


# 7.Write a generator that yields all two-digit even numbers.

# def even():
#     for i in range(10,100):
#         if i % 2 == 0:
#             yield i
# c=even()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# 8.Create a generator that takes a list of numbers and yields only those numbers that are greater than the previous number.

# def demo():
#     a=[1,2,3,4]
#     for i in a:
#         if a[i]>a[i-1]:
#             yield i
# c=demo()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


# 9.Write a generator that yields the ASCII value of each character in a string.
# s="aditya"
# def asc(s):
#     for i in s:
#         yield ord(i)
# c=asc(s)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))

# 10. Create a generator that yields numbers divisible by both 3 and 5 up to n.

# def demo():
#     for i in range(1,20):
#         if i%3==0 and i%5==0:
#             yield i
# c=demo()
# print(next(c))

# 11.Write a generator that yields characters of a string but skips digits.

# a="adi123tya"
# def demo(a):
#     for i in a:
#         if i.isalpha():
#             yield i
# c=demo(a)
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


# 12.Write a generator that yields elements from two lists alternately.
# a=[1,3,5]
# b=[2,4,6]
# # o/p: 1 → 2 → 3 → 4 → 5 → 6
#
# def demo(a,b):
#     for i in zip(a,b):
#         yield i
# c=demo(a,b)
# print(next(c))
# print(next(c))
# print(next(c))

# 13.Create a generator that yields each substring of a string starting from the first character.
# (e.g., "abc" → "a", "ab", "abc")

# a="abc"
# def demo(a):
#     for i in range(1,len(a)+1):
#         yield a[:i]
# c=demo(a)
# print(next(c))
# print(next(c))


# Nov 19 - 1:05 pm
# 14.Write a generator that yields only unique characters from a string, preserving the original sequence.
# Input: "banana"
# Output: b, a, n
# def demo():
#     s="banana"
#     z=""
#     for i in s:
#         if i not in z:
#             z+=i
#     yield z
# c=demo()
# print(next(c))
# print(next(c))
# print(next(c))


# 15.Generator that yields even numbers up to n

# def even():
#     for i in range(10):
#         if i % 2 == 0:
#             yield i
# c=even()
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))