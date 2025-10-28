#--> islower checks if all the charcter in lower case it will  return trur otherwise it will return false

# a='123aditya'
# print(a.islower())

#--> isupper checks if all the charcter in upper case it will  return trur otherwise it will return false

# b="##ADITYA123"
# print(b.isupper())

# count:--> it is used to count the number of character in a string
# in start index and in end index we can pass negative value also 

# a="welcome to my code"
# print(a.count("o"))

# find--> it find the postion of substring in a string

# a="welcome to my code"
# print(a.find("0"))-->gives o/p
# print(a.find("z"))-->gives o/p as -1 dont give any error

# index:-->it gives the position of the spcific char in string

# a="welcome to my code"
# print(a.index("m"))-->gives o/p
# print(a.index("z"))--> it gives value error

# strip-->it used to remove any char of white space from a string in startig and ending both also know a leading postion and trailing position

a="welcome to my code"

# print(a.trip('e'))
# print(a.rstrip("e"))
# print(a.lstrip("w"))

# print(a.upper())
# print(a.title())
# print(a.capitalize())
# print(a.split())

# import keyword
# # print("None" in keyword.kwlist)
# print(keyword.iskeyword("none"))

# s = "pyTHon"
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())

# print("123python".capitalize())
# print("@hello".capitalize())

# print("abc123".isalnum())
# print("abc 123".isalnum())
# print("123".isdigit())
# print("Ⅻ".isdigit())

# s = "###python###"
# print(s.strip('#'))
# print(s.lstrip('#'))
# print(s.rstrip('#'))

# s = "xyxyhelloxy"
# print(s.strip("xy"))

# a = "welcome to my code"
# print(a.find("z"))
# print(a.index("z"))

# a = 'python'
# print('-'.join(a))
# print(' '.join(a))
# print(''.join(reversed(a)))

# print("yellow".replace("l","*", 2000))

# print("hello".islower())
# print("HELLO123".isupper())
# print("Hello".islower())


# s = "python   is   great"
# print(s.split())
# print(s.split(' '))

# import keyword
# print(keyword.iskeyword("False"))
# print(keyword.iskeyword("false"))

# print("True".isidentifier())
# print("class".isidentifier())

# s = "pyTHon"
# print(s.capitalize())
# print(s.title())
# print(s.swapcase())


# print("123python".capitalize())
# print("@hello".capitalize())

# s = "heLLo WoRLd"
# print(s.title())
# print(s.capitalize())
# print(s.swapcase())


# a='aditya'
# print(a+'2005')
# a=5
# print("a"*5)

# 25-08-2025

# a=[]
# print(a)
# print(type(a))


# a=list()
# print(a)


# x={1,2,3,4,5}
# y={4,3}
# z={4,3,6}

# # print(x.issuperset(y))
# print(x.issuperset(z))


# x={1,2,3,4}
# y={1,2,3,4,5}
# z={1,2,3}
# print(x.issubset(y))
# print(x.issubset(z))


# x={1,2,3,4,4,5}
# y={1,7,8,9}
# print(y.intersection_update(x))
# print(y)

# x={1,2,3,4,5}
# y={1,7,9,5,10,11}
# print(x.symmetric_difference(y))
# print(x.symmetric_difference_update(y))
# print(x)


# conitional statement

# if 10<20:
#     print('10 is bigger')

# Q1.--> to check the number is even

# num=eval(input('Enter the number you want to check'))
# if num%2==0:
#     print( f'Your entered no {num} is even')---> Enter the number you want to check 10
# Your entered no 10 is even

# Q.2 ----> to check both number are odd

# num1=eval(input('Enter the number you want to check'))
# num2=eval(input('Enter the number you want to check'))
# if num1%2==1 and num2%2==1:
#     print(f'{num1} and {num2} are both odd number')

# Q3---> write a program to take 1 number from the user and if the number is odd then make the half of that nuber

# num=eval(input('Enter the number you want to check'))
# if num%2==1:
#     print( f'Your entered no {num/2} is trrueb half and {num//2} is round half') 

# Q4--->write a program to take a number from the user if there data type is float then make square of that num

# num=eval(input('Enter the number you want to check'))
# if type(num)==float:
#     print(f'{num**2}')

# Q5--->write a program to take 1 string from the user and check their data type is string is not if the datatype is string then reverse the string

# string = eval(input("Enter a string: "))
# if type(string) == str:
#     print(string[::-1])
#  or

# string = eval(input("Enter a string: "))
# if string.isalplha():
#     print(string[::-1])

# Q6--->write a program to take 1 list from the user and if the of th list  iseven thn reverse the list

# list = eval(input("Enter a list: "))
# if len(list)%2==0:
#     print(f'{list[::-1]} is reversed list')       

# Q7 -->write a program to check the data type of the user input if it is string if it is string then print last char of the string

# strr = eval(input("Enter a str: "))
# if type(strr)==str:
#     print(f'{strr[-1]}')

# or

# strr = eval(input("Enter a str: "))
# if isinstance(strr,str):
#     print(f'{strr[-1]}')

# Q.8 write a program to check given number is positive

# num=eval(input("enter a number:"))
# if num>0 or num==0:
#     print(f'{num} is positive')


# Q.9 write a program to check given number is negative

# num=eval(input("Enter a num:"))
# if num<0:
#     print(f'{num} is negative')

# Q.10 write a program to check given number is zero

# num=eval(input("Enter a num:"))
# if num==0:
#     print(f'the given number {num} is zero')

# Q.11 write a progarm check if the given program is divisble is by 5

# num=eval(input("enter a num:"))
# if num%5==0:
#     print(f'{num} is divisible by 5')

# Q.12 write a program to check if 88 is less than 100

# if 88<100:
#     print("yes 88 is less than 100")

# Q.13 write a program to check if it is 3 digit

# num=eval(input("Enter a num:"))
# # a=str(num)
# if len(str(num))==3:
#     print(f'{num} is three digit')

# or

# num=input("Enter a num:")
# # a=str(num)
# if len(num)==3:
#     print(f'{num} is three digit')

# Q.14 write a program to check if the string is in lower case

# str=eval(input("enter a str"))
# if str.islower():
#     print(f'{str} is in lower case')

# Q.14 write a program to check if the string is in upper case

# str=eval(input("enter a str"))
# if str.isupper():
#     print(f'{str} is in upper case')

# Q.14 write a program to check if the string is contain any space case

# str=eval(input("enter a str"))
# if str.isspace():
#     print('string conatins space') 

# Q14.write a program to check if the string start with capital letter

# str=eval(input("enter a str"))
# st=str[0]
# if st.isupper():
#     print(f'{str} start with a upper char') 

# Q15.write a program to check if the string contains only alphabtes

# str=eval(input("enter a str"))
# if str.isalpha():
#     print(f'{str} contains only character') 

# Q16.write a program to check if the string contains only digit

# str=eval(input("enter a str"))
# if str.isdigit():
#     print(f'{str} contains only character') 

# Q.13 write a program to check if the string ends with ('.')

# str=eval(input("enter a str"))
# if str.endswith('.'):
#      print(f'{str} ends with {'.'}') 

# or
 
# str=eval(input("enter a str"))
# st=str[-1]
# if st.endswith('.'):
#      print(f'{str} ends with {'.'}') 

# Q.14 write a program to check if 'a' is present in the string

# str=eval(input("enter a str:"))
# if 'a' in str:
#     print(f'{str} contains a')

# Q.15 using two input

# str=eval(input("enater a str:"))
# char=eval(input("enater a char:"))
# if char in str:
#     print(f'{str} contains {char}')

# 15. Write a program to check if the first and last characters of a string are the same (e.g., x = 'level'). 

# str=eval(input("Enter a string:"))
# # ch1=str[0]
# # ch2=str[-1]
# if str[0]==str[-1]:
#     print(f'both first and last char of {str} is same')

# 16. Write a program to check if a character is a vowel. (e.g., a = 'I')

# str=eval(input("Enter a string:"))
# if str in ('a','e','i','o','u'):
#     print(f'{str} is vowel')


# 17. Write a program to check if a character is uppercase. (e.g., b = 'P') 

# char=eval(input("Enter a char"))
# if char.isupper():
#     print(f'{char} is capital')

# or

# char=eval(input("Enter a char"))
# if 65<=ord(char)<=90:
#     print(f'{char} is upper')

# 18. Write a program to check if a character is lowercase. (e.g., c = 'k') 

# char=eval(input("Enter a char"))
# if char.islower():
#     print(f'{char} is capital')

# or


# 19. Write a program to check if a character is a digit. (e.g., ch = '5') 

# char=eval(input("Enter a char"))
# if char.isdigit():
#     print(f'{char} is capital')

# 20. Write a program to check if the ASCII value of a character is greater than 100. (e.g., z = 'd') 

# char=eval(input("Enter a char:"))
# ascii_value=ord(char)
# if ascii_value>100:
#     print(f'{char} is greate than 100')

# 21. Write a program to check if 5 exists in a list. (e.g., lst = [2, 4, 5]) 

# list=eval(input("enter a list:"))
# if 5 in list:
#     print(f'{list} conatins 5')

# 22. Write a program to check if the last element in a list is even. 
# (e.g., l = [1, 2, 4]) 

# list=eval(input("enter a list:"))
# last_ele=list[-1]
# if  last_ele%2==0:
#     print(f'{list} last ele is even')

# 23. Write a program to check if the first two elements in a list are the same. (e.g., lst = [5, 5, 9])

# list=eval(input("enter a list:"))
# first_ele=list[0]
# sec_ele=list[1]
# if  first_ele==sec_ele:
#     print(f'{list} first and second element in the list is same')

# 24. Write a program to check if the sum of a list is greater than 100. (e.g., y = [50, 40, 30]) 

# list=eval(input("enter a list:"))
# if sum(list)>100:
#     print(f'{list} has some more than')

# Q26 write a program to check if file name ends with 'txt'

# str=eval(input("enter a string:"))
# if str.endswith('txt'):
#     print(f'{str} ends with txt')

# or 

# str=eval(input("enter a string:"))
# if str[-1:-4:-1]=='txt':
#     print(f'{str} ends with txt')

# or 

# str=eval(input("enter a string:"))
# c=str.split('.')
# if c[-1]=='txt':
#     print(f'{str} ends with txt')

# num=eval(input("enter a adhar num:"))
# if len(num)==16 and num.isdigit():
#     print(f'{num} is validn adhar card')

# Q32.write a program to check if a given programming language is present in the list or not

# prm=eval(input('enter a language:'))
# p=['c','c++','java','python']
# if prm in p:
#     print(f'{prm} is present in {p}')

# Q.check if the first char is consonent or not

# str=eval(input("enter"))
# if str[0] not in ('a','e','i','o','u','A','E','I','O','U'):
#     print(f'{str} stats with {str[0]} and {str[0]} is consonent')

# Q.write a program to check if is the number is even then store the number in list

# num=eval(input('enter a num:'))
# l=[]
# if num%2==0:
#     l.append(num)
#     print(f'{num} is even')
#     print(l)

# num=eval(input("enter a char"))
# d={}
# if num.isalpha():
#     d[num]=ord(num)
#     print(d)

# str=eval(input("enter a char:"))
# d={}
# if str.isupper():
#     c=str.lower()
#     print(c)
#     d[c]=ord(c)
#     print(d)

# char=eval(input("Enter a char:"))
# d={}
# if 'A'<=char<='Z':
#     c=ord(char)+32
#     # ----- here 32 is the differnce between asciii
#     # value capital letter and small char
#     d[c]=chr(c)
#     print(d)

# if else question

# 1.to check no if even or odd'

# num=eval(input("enter a num:"))
# if num%2==0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd')

# 2.check num is three digit or not

# num=eval(input("enter a num:"))
# if len(str(num))==3:
#     print(f'{num} is three digit')
# else:
#     print(f'{num} is not three didgit')

#3.
# num=eval(input("enter a age:"))
# if num>=18:
#     print(f'{num} eligible for voting')
# else :
#     print(f'{num} is not eligible')

# 4.
# age=eval(input("enter a age:"))
# if age>=60:
#     print(f'{age} you are senior citizen')
# else :
#     print(f'{age} is not senior citizen')

#5.
# num1=eval(input("enter num1"))
# num2=eval(input("enter num2"))
# if num1<num2:
#     print(f'{num1} is lowest')
# else:
#     print(f'{num2} is lowest')

# 6.
# num1=eval(input("enter num1"))
# num2=eval(input("enter num2"))
# if num1>num2:
#     print(f'{num1} is greater')
# else:
#     print(f'{num2} is greater')

#7.

# num1=eval(input("enter num1: "))
# if num1>0:
#     print(f'{num1} is positive')
# else:
#     print(f'{num1} is negative')

# 7.
# num1=eval(input("enter num1: "))
# if num1<=100:
#     print(f'{num1*5} is the bill')
# else:
#     print(f'{num1*8} is the bill')


