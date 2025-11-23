# #FOR LOOP  level one questions


# 1.wap to print the number form 1 -20 segregate even and odd number into list

# e=[]
# o=[]
# for i in range(1,21):
#     if i%2==0:
#         e.append(i)
#     else:
#         o.append(i)
# print(e,o)

# 2.wap to extract vowels and digits in a string

# s="hello123"
# for i in s:
#     if i in 'aeiou' or i.isdigit():
#         print(i,end="")

# 3.wap to capitalize only the first letter of every word in the given list
# l=["vaidegi","rahul","shivam","kapil","patil"]
# for i in l:
#     print(i.capitalize())

# 4.wap to extract only individual data types form the list

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# for i in l:
#     if isinstance(i,(int,float,bool,complex)):
#         print(i)

# 5.wap to extract only individual data types from the list and sum all the individual data types
# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]

# l=["hello",1,23.4,5+6j,"guys",[2,3,4],True,False]
# l2=[]
# for i in l:
#     if isinstance(i,(int,float,bool,complex)):
#         l2.append(i)
# print(sum(l2))


# 6.wap to print the count of alphabets and numbers and space in the given string
# s="india got the independence in the year 1947"
# alcount=0
# nocount=0
# spcount=0
# for i in s:
#     if i.isalpha():
#         alcount=alcount+1
#     elif i.isnumeric():
#         nocount=nocount+1
#     else:
#         spcount=spcount+1
# print(alcount,nocount,spcount)

# 7.wap to check how many words are present in the given sentence
# s="hello world sentence"
# wcount=1
# for i in s:
#     if i==" ":
#         wcount=wcount+1
# print(wcount)


# 8.wap to create a dictionary and print the characters 
# and its Ascii value pair
# s="hello world"
# output:--> {"h":ascii value,"e":ascii value........}

# s="hello world"
# d={}
# for i in s:
#     d[i]=ord(i)
# print(d)

# 9.wap to create a dictionary and traverse into it and if the length is even print as it else reverse it

# names=["apple","google","yahoo","microsoft","gmail","walmart"]

# output:-->{'apple': 'elppa', 'google': 'google', 'yahoo': 'oohay', 'microsoft': 'tfosorcim', 'gmail': 'liamg', 'walmart': 'tramlaw'}

# names=["apple","google","yahoo","microsoft","gmail","walmart"]
# d={}
# for i in names:
#     if len(i)%2==0:
#         d[i]=i
#     else:
#         d[i]=i[::-1]
# print(d)


# 10.wap to print series of factorial(take user input)

# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a:
#     print(i*i)

# 11.wap to create a dictionary with element and its count pair


# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# output:-->
# {'yellow': 2, 'red': 2, 'black': 1, 'pink': 2, 'orange': 1, 'green': 1}

# l=["yellow","red","black","pink","orange","green","red","pink","yellow"]
# d={}
# for i in l:
#     d[i]=l.count(i)
# print(d)

# 12.wap to find the length of the string without using inbuilt function
# s="Never Give Up"
# l=0
# for i in s:
#    l=l+1
# print(l) 


# 13.wap to reverse a string without using inbuilt function
# x="you did it guys"
# for i in x[::-1]:
#     print(i,end="")

# 14.wap to print alternative character from a given string
# s="hello python"
# for i in range(0,len(s),2):
#     print(s[i],end="")

# for loop level 2 questions
# **********************************


# 15.wap to create a dictionary index and word pair
# s="tomorrow is weekend and non-veg special"
# o/p:-->{0: 'tomorrow', 1: 'is', 2: 'weekend', 3: 'and', 4: 'non-veg', 5: 'special'}

# s="tomorrow is weekend and non-veg special"
# l=s.split()
# d={}
# for i in l:
#     d[l.index(i)]=i
# print(d)

# 16.wap to create a dictionary words and its length pair
# s="tomorrow is weekend and non-veg special"

# s="tomorrow is weekend and non-veg special"
# l=s.split()
# d={}
# for i in l:
#     d[i]=len(i)
# print(d)
# o/p:-->{'tomorrow': 8, 'is': 2, 'weekend': 7, 'and': 3, 'non-veg': 7, 'special': 7}




# 17.wap to create a dictionary characters and its corresponding upper case characters
# s="sunday"
# o/p:-->{'s': 'S', 'u': 'U', 'n': 'N', 'd': 'D', 'a': 'A', 'y': 'Y'}

# s="sunday"
# d={}
# for i in s:
#     d[i]=i.upper()
# print(d)

# 18.wap to create a dictionary Ascii and character pair
# l=[89,51,111,77,108,120]
# o/p:-->{89: 'Y', 51: '3', 111: 'o', 77: 'M', 108: 'l', 120: 'x'}

# l=[89,51,111,77,108,120]
# d={}
# for i in l:
#     d[i]=chr(i)
# print(d)

# 19.wap to  create a list of characters and its Ascii value pair
# s="sunday"
# o/p:-->[('s', 115), ('u', 117), ('n', 110), ('d', 100), ('a', 97), ('y', 121)]

# s="sunday"
# l=[]
# for i in s:
#     l.append((i,ord(i)))
# print(l)

# 20.WAp to perform clear() in list without using inbuilt method
# s=[1,2,3,4,5,7]
# for i in range(len(s)):
#     s.pop()
# print(s)

# 21.wap to create a dictionary with words and its length pair and ends with vowel
# s="Today is Tuesday and attending python session"
# l=s.split()
# d={}
# for i in l:
#     if i[-1] in 'aeiou':
#         d[i]=len(i)
# print(d)

# 22.wap to create a dictionary with letter and its words starting with that letter pair

# s="hi hello good morning welcome to python session"
# d={}
# for i in s.split():
#     if i[0] not in d:
#         d[i[0]]=[i]
#     else:
#         d[i[0]]+=[i]
# print(d)







# o/p:-->{'h': ['hi', 'hello'], 'g': ['good'], 'm': ['morning'], 'w': ['welcome'], 't': ['to'], 'p': ['python'], 's': ['session']}




# 23.wap to create a dictionary of characters and its indices pair
# s="hello python"
# d={}
# for i in range(len(s)):
#     if s[i] not in d:
#         d[s[i]]=[i]
#     else:
#         d[s[i]]+=[i]    
# print(d)
# o/p:-->{"h":[0,9],"e":1..........}


# 24.wap to create a dictionary word and reverse word pair
# s="tomorrow is weekend and non-veg special"
# l=s.split()
# d={}
# for i in l:
#     d[i]=i[::-1]
# print(d)
# o/p:-->{'tomorrow': 'worromot', 'is': 'si', 'weekend': 'dnekeew', 'and': 'dna', 'non-veg': 'gev-non', 'special': 'laiceps'}


# 25.Reverse a list without using any built-in functions and slicing.
# l = [1, 2, 3, 4]
# for i in l[::-1]:
#     print(i,end=" ")





# ASSIGNMENT QUESTIONS


# 1.wap to Sum of numbers
# s = 'Sony12India567pvt21ltd'
# l=[]
# for i in s:
#     if i in '0123456789' :
#         c=int(i)
#         # print(c)
#         l.append(c)
# print(sum(l))


# 2.Print all the missing numbers from 1-10 in the below list
# l = [1, 2, 3, 4, 6, 7, 10]
# l2=[]
# for i in range(1,10):
#     if i not in l:
#         l2.append(i)
# print(l2)        
    
# 3.WAP to remove duplicates from the list without using inbuilt function
# d=[1,2,3,4,5,6,7,1,2,3,4]
# d1=[]
# for i in d:
#     if d.count(i)<=1:
#         # print (i)
#         d1.append(i)
# print(d1)

# 4.wap to replace all the character with "-" if the characters occurs more than once in a string
# s="hellohai"

# for i in s:
#     if s.count(i)>1:
#         s=s.replace(i,'-')
# print(s)
# o/p---->-e--o-ai

        

# 5.WAP to print all numeric values in a list
# l = ['apple', 123, 'google', '45.6', 'yahoo', [1,2,3],True, (1,3,7), 6+3j]  
# for i in l:
#     if isinstance(i,(int,complex,float)):
#         print(i)

# For loop questions day---->3

# 1.wap to print first and last char of each name in the list
# a=["Sunil","anil","Suresh","Mahesh","Dinesh"]
# for i in a:
#     print(i[0],i[-1])


# 2.wap to create a new list as square of each number of below list
# b=[2,4,5,6,7,1]
# c=[]
# for i in b:
#     c.append(i*i)
# print(c)


# 3.wap if number is even the print its square else print its cube
# c=[2,4,5,3,7,9]
# for i in c:
#     if i%2==0:
#         print(i*i)
#     else:
#         print(i*i*i)

# 4.wap to create a list with square and cube of each numbers
# d=[2,4,5,1,8,9,10]
# d1=[]
# for i in d:
#    d1.append((i*i,i*i*i)) 
# print(d1)
# o/p-->[(4, 8), (16, 64), (25, 125), (1, 1), (64, 512), (81, 729), (100, 1000)]



# 5.wap to create a new list of reversing each name from the list
# names=["prince","Rekha","Madhu","Sindhu","denga","manga"]
# rev=[]
# for i in names:
#     rev.append(i[::-1])
# print(rev)
# op:['ecnirp', 'ahkeR', 'uhdaM', 'uhdniS', 'agned', 'agnam']

# 6.wap to create a new list, of individual and collection data type from list
# data=[20.12,True,[10,20],"super",{1,2},{"a":10},100,(8,9)]
# ind=[]
# coll=[]
# for i in data:
#     if isinstance(i,(int,float,bool,complex)):
#         ind.append(i)
#     else:
#         coll.append(i)
# print(ind,coll)
# op:[20.12, True, 100] [[10, 20], 'super', {1, 2}, {'a': 10}, (8, 9)] 


# 7.wap to print author name in books dictionary
# books={"love story":["Harish",30],"biography":["padam",150],"animals":["vimala",75]}
# for i in books.values():
#     print(i[0],end=",")

# 8.wap to create a dictionary characters and its count pair
# char=["a","M","i","A","M","I","i","H","a","H"]
# d={}
# for i in char:
#     d[i]=char.count(i)
# print(d)

# 9.wap to group fruit name and country pair
# from itertools import zip_longest
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
# for i in zip_longest(d,p.values()):
#     print(*i)


# 10.wap to group fruit name and country pair only if a fruit is even length
# from itertools import zip_longest
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"India","America":"us","UK":"Toronto","Africa":"Uganda"}
# for i,j in zip_longest(d,p.values()):
#     if len(i)%2==0:
#         print(i,j)


# 11.wap to sum of same index element from l1,l2,l3
# from itertools import zip_longest
# l1=[10,20,30,40]
# l2=[78,44,11,99]
# l3=[1,2,3,4]
# l4=[]
# for i in range(len(l1)):
#     t=l1[i]+l2[i]+l3[i]
#     l4.append(t)
# print(l4)

# 12.wap to pair values of both dictionary
# from itertools import zip_longest
# d={"apple":45,"mango":67,"cherry":90,"berry":23}
# p={"Kashmir":"india","America":"us","UK":"Toronto","Africa":"Uganda"}
# for i in zip_longest(d.values(),p.values()):
#     print(*i)

# 13.WAP to print sum of internal and external list
# l = [[1,2,3], [4,5,6], [7,8,9]]
# l2=[]
# for i in l:
#     c=sum(i)
#     print(c,end=",")
#     l2.append(c)
# print(sum(l2))
# output:-->
#    #internal = 6, 15, 24
#    #external --> 45

# 14.wap to using this list get the below output

# l = ['sun flower', 'Lilly flower', 'Marigold flower', 'lion animal', 'tiger animal', 'eagle bird', 'snake animal', 'lotus flower', 'pigeon bird']
# d={}
# for i in l:
#     s=i.split()
#     if s[1] not in d:
#         d[s[1]]=[s[0]]
#     else:
#          d[s[1]]+=[s[0]]
# print(d)

# o/p:-->{'flower': ['sun', 'Lilly', 'Marigold', 'lotus'], 'animal': ['lion', 'tiger', 'snake'], 'bird': ['eagle', 'pigeon']}

# --------------------------------------------------------------------------

# 1.Print numbers divisible by 3 and 5 between 1–100

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)

# 2.Count vowels in a string
# s = "Data Science With Python"
# count=0
# for i in s:
#     if i in 'aeiou':
#         count+=1
# print(count)

# 3.Sum of digits of a number
# n=9875
# s=str(n)
# l=[]
# for i in s:
#     c=int(i)
#     # print(c)
#     l.append(c)
# print(sum(l))

# 4.Sum of first 20 natural numbers

# 5.Multiply each element by 5
# s=[2,4,6,8]
# o/p--[10,20,30,40]

# 6.Print square of numbers 1–10
# for i in range(1,11):
#     print(i*i)

# 7.Print characters at even index
# s = "PYTHON"
# for i in range(0,len(s),2):
#     print(i)

# 8.Print sum of even numbers between 1–100
# for i in range(1,101):
#     if i%2==0:
#         print(i)

# 9.Separate positive & negative numbers
# lst = [12, -5, 7, -9, 33, -2]
# po=[]
# ne=[]
# for i in lst:
#     if i>0:
#         po.append(i)
#     else:
#         ne.append(i)
# print(po,ne)



# 10.Convert list of words to uppercase
# words = ["apple", "orange", "banana"]
# for i in words:
#     print(i.upper())


#1.wap to check the given element is palindrome (without slicing)
# a="madam"
# res=""
# for i in range(len(a)-1,-1,-1):
#     res=res+a[i]
# if a==res:
#         print("palindrome")
# else:
#         print("not palindrome")

#2.Remove duplicate characters but keep order
# b="banana"
# c=''
# for i in b:
#     if i not in c:
#         c=c+i
# print(c)
        
#3.Swap uppercase and lowercase
# c="HeLLo"
# s=''
# for i in c:
#     if i.isupper():
#         s=s+i.lower() 
#     else:
#         s=s+i.upper()
# print(s)


#4.Common characters of both words
# from itertools import zip_longest
# x='apple'
# y='grapes'
# for i in x:
#     if i in y:
#         print(i)

              



#5.Remove digits in the given string
# w="a1b2c3d4"
# c=""
# for i in w:
#     if i not in "0123456789":
#         c=c+i
# print(c)
        

#6.wap to print only Characters appearing exactly once
# d= "success"
# c=''
# for i in d:
#     if d.count(i)==1:
#         c=c+i
# print(c)


#7.Count how many times each vowel appears
# e= "beautiful language"
# count=0
# for i in e:
#     if i in 'aeiou':
#         count+=1
# print(count)

#8.Print only non-alphabet characters
# f= "Hello123 @World"
# c=''
# for i in f:
#     if not ('A'<=i<='Z' or 'a'<=i<='z'):
#         c=c+i
# print(c)


#9.wap to count only consonants
# g= "education"
# count=0
# for i in g:
#     if i not in 'aeiou':
#         count+=1
# print(count)

#10.wap to Remove all vowels but keep spaces
# h= "hello world"
# c=''
# for i in h:
#     if i not in 'aeiou':
#         c=c+i
# print(c)

#11.Count words starting with vowel
# s = "apple is a useful fruit"
# count=0
# c=s.split()
# # print(c)
# for i in c:
#     if i[0] in 'aeiou':
#         count=count+1
# print(count)


#12.Print words longer than 5 characters
q = "Python programming is interesting"

#13.wap to remove duplicate words
z= "this is is python python class"

#14.wap to print Even index uppercase, odd lowercase
# w1= "pythonprogramming"
# for i in range(len(w1)):
#     if i%2==0:
#         print(chr(ord(w1[i])-32))
#     else:
#         print(chr(ord(w1[i])))
        
    


#15.wap to print below pattern
s="cat"
# # c
# # ca
# # cat
# res=''
# for i in s:
#     res+=i
#     print(res)

    
    