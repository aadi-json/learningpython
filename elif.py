#wap to check the given number is +ve/-ve/0

# num=eval(input("enter a number------> "))
# if num<0:
#     print(f'{num} is -ve')
# elif num>0:
#     print(f'{num} is +ve')
# else:
#     print(f'{num} is zero')

# ------------------------------------------------------------------------------------

#wap to check the given element is upper/lower/number

# ele=eval(input("enter a ele--------> "))
# if ele.isupper():
#     print(f'{ele} is uppercase')
# elif ele.islower():
#     print(f'{ele} is a lower')
# elif ele.isdigit():
#     print (f'{ele} is a digit')

# -------------------------------------------------------------------------------
# ele=eval(input("enter a ele--------> "))
# if 65<=ord(ele)<=90:
#     print(f'{ele} is uppercase')
# elif 97<=ord(ele)<=122:
#     print(f'{ele} is a lower')
# elif 47<=ord(ele)<=56:
#     print (f'{ele} is a digit')
# else:
#     print(f'{ele} is special character')

# ------------------------------------------------------------------------------------

#wap to check which number is greater amoung 3 number
# a=45
# b=75
# c=66
# if a>b and a>c:
#     print("a is greater")
# elif b>c and b>a:
#     print("b is greater")
# else:
#     print("c is greater")

# -------------------------------------------------------------------------------------

# 2.wap to check a data is a sequence/iterable/individual data type

# data=eval(input("enter the data------> "))
# if type(data) in (int,bool,complex,float):
#     print(f'{data} is single valued')
# elif type(data) in (list,str,tuple):
#     print(f'{data} is sequential')
# elif type(data) in (set,dict):
#     print(f'{data} is iterable')
# else:
#     print(f'{data} is invalid')

# -------------------------------------------------------------------------------------

# 3.wap if input is string return its length,else if input is
# list pop element,else if input is tuple reverse else invalid input

# data=eval(input("enter a data------> "))
# if type(data)==str:
#     print(f'{data} is string and lenght is {len(data)}')
# elif type(data)==list:
#     print(f'{data} is list and poped element is {data.pop()}')
# elif type(data)==tuple:
#     print(f'{data} is tuple and reverse tuple is {data[::-1]}')
# else:
#     print(f'{data} is invalid')

# ------------------------------------------------------------------------------------

# 5.wap to take marks of 5 sub,calculate the average if the average
# is b/w 90-100 print Distinction
# if 75-89 print first class and if it('s 60-74 print second class,'
# ' if 50-59 print Third class,below 50 is fail)
# note:-->max marks is 100

# sub1=eval(input("enter the Marks"))
# sub2=eval(input("enter the Marks"))
# sub3=eval(input("enter the Marks"))
# sub4=eval(input("enter the Marks"))
# sub5=eval(input("enter the Marks"))
# avg=((sub1+sub2+sub3+sub4+sub5)/5)
# if 90<=avg<=100:
#     print(f'{avg}:distinction')
# elif 75<=avg<=89:
#     print(f'{avg}:first class')
# elif 60<=avg<=74:
#     print(f'{avg}:second class')
# elif 50<=avg<=59:
#     print(f'{avg}:third class')
# else:
#     print(f'{avg}:fail')

# ----------------------------------------------------------------------------------

# 1.Check if number is divisible by 3, 5, or both

# num=eval(input("enter a number----> "))
# if num%3==0 and num%5==0:
#     print(f'{num} is divisible by both 5 and 3')
# elif num%5==0:
#     print(f'{num} is divisible by 5')
# elif num%3==0:
#     print(f'{num} is divisible by 3')
# else:
#     print(f'{num} is not valid')

# ----------------------------------------------------------------------------------

# 2.Given a student's percentage, assign grade A (>=85), B (>=70), C (>=50), or Fail.

# per=eval(input("enter percentage--------> "))
# if per>=85:
#     print(f'{per}:A')
# elif per>=70:
#     print(f'{per}:B')
# elif per>=50:
#     print(f'{per}:c')
# else:
#     print(f'{per}:F')
    
# ------------------------------------------------------------------------------------

# 3.Decide ticket price category: Child (<12), Teen (12–17), Adult (18–59), Senior (60+)

# age=eval(input("enter age-----> "))
# if age<12:
#     print(f'{age}:350rs')
# elif 12<=age<=17:
#     print(f'{age}:500rs')
# elif 18<=age<=59:
#     print(f'{age}:700rs')
# elif age>=60:
#     print(f'{age}:200rs')

# ----------------------------------------------------------------------------------

# 4.Given temperature, print Very Cold (<0), Cold (<15), Mild (<25), Warm (<35), Hot

# temp=eval(input("enter the tempreture----------> "))
# if temp<0:
#     print(f'very cold')
# elif temp<15:
#     print("cold")
# elif temp<25:
#     print("mild")
# elif temp<35:
#     print("warm")
# else:
#     print("very hot")

# 5.Given a password, classify strength: Very Weak, Weak, Medium, Strong

# password=eval(input("enter a password---------> "))
# if len(password)<3:
#     print("very weak")
# elif len(password)<5:
#     print("weak")
# elif len(password)<8:
#     print("medium")
# elif len(password)<12:
#     print("strong")
# else:
#     print("very strong")

# 6.Given a filename, identify type: Python, Text, Image, Other.

# filename=eval(input("enter a file-------> "))
# if filename.endswith('.py'):
#     print("its python file")
# elif filename.endswith('.txt'):
#     print("its txt file")
# elif filename.endswith('.img'):
#     print("its img file")
# else:
#     print("its other file")


# 7.For a day number (1–7), print weekday name or Invalid day.

# day=eval(input("enter a day--------> "))
# if day ==1:
#     print("sunday")
# elif day==2:
#     print("monday")
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wensday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# else:
#     print("saturday")


# 8.For a credit score integer, categorize Poor, Fair, Good, Very Good, Excellent.

# score=eval(input("enter your credit score--------> "))
# if score<=100:
#     print("poor")
# elif score<=200:
#     print("fair")
# elif score<=300:
#     print("good")
# else:
#     print("excellent")

# -----------------------------------------------------------------------------------

# 1.  Tax Slab Calculator
#  Write a program that takes annual income as input and calculates tax:
# Up to ₹2,50,000 → No tax
# ₹2,50,001–₹5,00,000 → 5%
# ₹5,00,001–₹10,00,000 → 20%
# Above ₹10,00,000 → 30%

# ann_income=eval(input("enter a number--------> "))
# if ann_income<=250000:
#     print("no tax")
# elif 250001<=ann_income<=500000:
#     print("5 % tax")
# elif 500001<=ann_income<=1000000:
#     print("20% tax")
# elif ann_income>1000001:
#     print("30%")

# ------------------------------------------------------------------------------------

# 8.wap to perform list operations user should
# enter only list data type,if options 1 pop().
# options 2 sort() options 3 clear()
# invalid options,invalid data type

# data=eval(input("enter list data------> "))
# if isinstance(data,list)==True:
#     print("valid data")
#     options=eval(input("enter your options 1,2,3-------> "))
     
#     if options==1:
#         data.pop()
#         print(data)
#     elif options==2:
#         data.sort()
#         print(data)
#     elif options==3:
#         data.clear()
#         print(data)
#     else:
#         print("invalid options")
# else:
#     print("invalid data")

# -----------------------------------------------------------------------------------

# 3.wap to validate facebook username and password
# condition is:---> username-->"python"  and password="python masters"

# print("lets login to facebook")
# username=eval(input("enter your user name : "))
# if username=="python":
#     print(f'the given username {username} is found')
#     password=eval(input("enter your password"))
#     if password=='python master':
#         print("password is matched")
#         print("succesful logged in ")
#     else:
#         print("password does not match")
# else:
#     print("username does not match")

# ------------------------------------------------------------------------------------

#2.wap to check the given number is odd and divisible by 7

# num=eval(input("enter a number : "))
# if num%2==1:
#     print("number is odd")
#     if num%7==0:
#         print("number is divisible by 7")
#     else:
#         print("number is does not divisible 7")
# else:
#     print("num is even")

# ---------------------------------------------------------------------------------

# wap to check the given number is even and greater than 10

# num=eval(input("enter a number : "))
# if num>10:
#     print(f'{num} is greater than 10')
#     if num%2==0:
#         print(f'{num} is even')
#     else:
#         print(f'{num} is odd')
# else:
#     print(f'{num} is less than 10')

# -----------------------------------------------------------------------------

# 4.wap to Book ticket in Book my show
#
# condition:---> first it should ask theaters name then it should
# display the movie available
#then it has to display ticket price and in the end ticket
# should be booked

# print("<-------movie booking app---------------->")
# theater=eval(input("enter theater: "))
# if theater in ['pvr','inox','miraj','imax']:
#     print(f'{theater} found')
#     print("COOLIE,RRR,KGF")
#     movies=['COOLIE','RRR','KGF']
#     movie=eval(input("choose a movie"))
#     if movie in movies:
#         print(f'{movie} choosed')
#         price=[1000,2000,500]
#         pri=eval(input("chooose price (1000/2000/500)"))
#         if pri in price:
#             print(f'movie booked and the bill is {pri}')
#         else:
#             print("prince not found")
#     else:
#         print("movie does not found")
# else:
#     print("theater not found")

# ----------------------------------------------------------------------------------


paymennt_mode=['cash','credit-card','debit-card']
print(paymennt_mode)
mode=eval(input("enter payment mode"))
if mode in paymennt_mode:
    print("user used credit card")
    num_of_product=eval(input("enter no of product you purchased"))
    if num_of_product>=3:
        print(f'User enterd{num_of_product}')
        amount= eval(input('enter amount'))
        if amount>500:
            print(f'{amount*0.10}')
        else:
            print("not valid")
    else:
        print("enter more or equl to 3")
else:
    print("not valid")
    