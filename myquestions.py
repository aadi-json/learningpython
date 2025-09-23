# Write a program to check if a number is divisible by both 2 and 3.

# num=eval(input("Enter a Num:"))
# if num%2==0 and num%3==0:
#     print(f'{num} is divisible by both 2 and 3')

# Write a program to check if a number is between 50 and 100.

# num=eval(input("enter a num:"))
# if 50<=num<=100:
#     print(f'{num} is between 50 and 100')

# Write a program to check if a number is greater than the cube of 5.

# num=eval(input("enter a num:"))
# if num>5**3:
#     print(f'{num} is greater than cube of 5')

# Write a program to check if a number is equal to the reverse of another number.

# num=eval(input("enter 1st num:"))
# num2=eval(input("Enter 2nd  num"))
# if num==num2[::-1]:
#     print(f'{num} is reverse {num2}')

# Write a program to check if the difference of two numbers is even.

# num1=eval(input("enter 1st num:"))
# num2=eval(input("Enter 2nd  num:"))
# num3=num1-num2
# if num3%2==0:
#     print(f'the differnce of both {num1} and {num2} is even {num3}')


# Write a program to check if the sum of two numbers is greater than 100.

# num1=eval(input("enter 1st num:"))
# num2=eval(input("Enter 2nd  num:"))
# num3=num1+num2
# if num3>100:
#     print(f'the sum of {num1} and {num2} is greater than 100')

# Write a program to check if a string contains only vowels.

# str=eval(input('Enter a string:'))
# if str[0:len(str)] in 'aeiouAEIOU':
#     print(f'{str} contains only vowel')

# Write a program to check if a string contains any digit.

# str=eval(input('Enter a string:'))
# if str.isdigit():
#     print(f'{str} contains only digit')

# Write a program to check if the first and last characters are different.

# str=eval(input('Enter a string:'))
# if str[0]!=str[-1]:
#     print(f'{str} start and end char are different')

# Write a program to check if a year is a leap year.

# year=eval(input("enter a year:"))
# if year%400==0:
#     print(f'{year} is a leap year')

# Write a program that takes three numbers from the user and prints the largest of the three.

# num1=eval(input('enter num1:'))
# num2=eval(input('enter num2:'))
# num3=eval(input('enter num3:'))
# if num1>num2 and num1>num3:
#     print(f'{num1} is greater')
# if num2>num3 and num2>num1:
#     print(f'{num2} is greater')
# if num3>num1 and num3>num2:
#     print(f'{num3} is greater')

# Write a program to take a user's input for their score (out of 100) and display their grade: 'A' for 90-100, 'B' for 80-89, 'C' for 70-79, and 'F' for below 70.

# num=eval(input("Enter a num:"))
# if 90<=num<=100:
#     print(f'{num}:`A`')
# if 70<=num<=89:
#     print(f'{num}:`B`')
# if 70<=num<=79:
#     print(f'{num}:`C`')
# if num<70:
#     print(f'{num}:`F`')

# Write a program that takes three side lengths of a triangle and determines if it is equilateral, isosceles, or scalene.

# num1=eval(input('Enter a num1:'))
# num2=eval(input('Enter a num2:'))
# num3=eval(input('Enter a num3:'))

# if num1==num2==num3:
#     print("it is euilateral triangle")
# if num1==num2 or num2==num3 or num3==num1:
#     print("it is isosceles")
# if num1!=num2!=num3:
#     print("it is scalene")

# Write a program to check if a number is a "buzz number" (it is divisible by 7 or ends with the digit 7).

# num=eval(input("Enter a num:"))
# if num%7==0 or num%10==7:
#     print(f'{num} is buzz number')


# year=eval(input("Enter a year:"))
# if year%100==0:
#     print(f'{year} is a century year')
# else:
#     print(f'{year} not a century year')

# num=eval(input("Enter a num:"))
# if num<0:
#     print(f'{abs(num)}')
# else:
#     print(f'{num}')

# or

# without using inbuilt function

# num=eval(input("Enter a num:"))
# if num<0:
#     print(f'{-(num)}')
# else:
#     print(f'{num}')

# ang1=eval(input("enter value :"))
# ang2=eval(input("enter value :"))
# ang3=eval(input("enter value :"))

# if ang1+ang2+ang3==180:
#     print(f'it is tringle')
# else:
#     print(f'not a tringle')

# num1=eval(input("enter a num : "))
# if num1%9==0 or num1%6==0:
#     print(f'yes {num1} is divisible by 9 or 6')
# else:
#     print(f'no {num1} is not divible by 9 or 6 ')

# tup=eval(input("enter a tuple : "))
# if type(tup[0])==type(tup[1]) and len(tup)==2:
#     print("yes")
# else:
#     print("not")

# str=eval(input("enter a str:"))
# if str!=str[::-1]:
#     print(f'{str[::-1]}')
# else:
#     print(f'{len(str)}')

# inp=eval(input("enter value"))
# if type(inp)!=str or type(inp)!=tuple:
#     print(f'yes mutable')
# else:
#     print(f'its immutablle')

# or

# inp=eval(input("enter value"))
# if isinstance(inp,(list,set,dict)):
#     print('yes mutable')
# else:
#     print('its is immutable')

# import keyword
# s = input("Enter a string: ")
# if keyword.iskeyword(s):
#     print("Yes, it is a keyword")
# else:
#     print("Not a keyword")
#  or

# import keyword
# s = input("Enter a string: ")
# k=keyword.kwlist
# if s in k:
#     print("Yes, it is a keyword")
# else:
#     print("Not a keyword")

# 1.wap to check the given number is even or odd (take user input)

# num=eval(input("enter a number : "))
# if num%2==0:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd')

# 2.wap to check whether the male and female are eligible for wedding (take user input)

# male_age=eval(input("Enter your age as male : "))
# female_age=eval(input("Enter your age as female : "))
# if male_age>=21 and female_age>=18:
#     print("valid for marrige")
# else:
#     print("Not valid for marrige")

# 3.wap to return uppercase if the char is lower,else return same char (by taking user input)

# char=eval(input("Enter a character"))
# if char.islower():
#     print(f'{char.upper()}')
# else:
#     print(f'{char}')

# 5.wap to find greater value among the two number n1=34 n2=54

# n1=34
# n2=54
# if n1>n2:
#     print(f'{n1} is greater')
# else:
#     print(f'{n2} is greater')

# 6.wap to check if the given number is even or not,if it is not even add+1 and make it even (take user input)

# num=eval(input("Enter a number : "))
# if num%2==0:
#     print(f'{num} is even')
# else:
#     print(f'{num+1} made it even')

# 7.wap to check whether the first character in the given string is starting with uppercase or Not if it is not Then capitalize it s="python"

# s="python"
# if s[0]==s.isupper():
#     print(f'{s}')
# else:
#     print(f'{s.capitalize()}')

# 8.wap to check if the given number is even ,if it is even reduce it to its Half else make exponent (take user input)

# num=eval(input("Enter your num : "))
# if num%2==0:
#     print(f'{num/2}')
# else:
#     print(f'{num**num}')

# 9.wap to check number should be divisible by 3 and 7 (take user input)

# num=eval(input("Enter your num : "))
# if num%3==0 and num%7==0:
#     print(f'{num} is divisble by 3 and 7')
# else:
#     print(f'{num} is not divisible by 3 and 7')

# 10.wap if the length of string is even then reverse else convert into upper case (take user input)

# str=eval(input("Enter a string"))
# if len(str)%2==0:
#     print(f'{str[::-1]} reversed string')
# else:
#     print(f'{str.upper()} converted to uppercase')

# 11.wap to check a number is +ve/-ve number (take user input)

# num=eval(input("Enter a num : "))
# if num<0:
#     print(f'{num} is negative')
# else:
#     print(f'{num} is positive')

# 12.wap to check a data is individual or collection data type or not (take user input)

# data=eval(input("Enter a number : "))
# if isinstance(data,(int,bool,float,complex)):
#     print(f'{data} is individual')
# else:
#     print(f'{data} is collection')

# 13.wap to check whether the specified character is present in the given string s="Python"

# s="Python"
# char=eval(input("Enter a char : "))

# if char in s:
#     print(f'{char} is present in {s}')
# else:
#     print(f'{char} is not present {s}')

# 14.wap to check the length of dictionary and length of dictionary is even or Not if even
# print as it is or else add a item and make it even
#D={"a":"apple","b":"ball","c":"cat"}

# dict=eval(input("Enter a dict : "))
# if len(dict)%2==0:
#     print(f'{dict}')
# else:
#    dict[10]="hii"
#    print(dict)

# 15.wap to check the given number is greater than 5,if it is greater convert that number into negative number
# else print the same number

# num=eval(input("Enter a number : "))
# if num>5:
#     print(f'-{num}')
# else:
#     print(f'{num}')

# 17.wap to check the given number is odd, if it is odd divide it by 2 and print reminder and quotient else print it is even (take user input)
 
# num=eval(input("Enter a number : "))
# if num%2!=0:
#     a,b=divmod(num,2)
#     print(f'{num/2} and {a,b}')
# else:
#     print(f'{num} is even')

# 18.wap to check if the given character is alphabets or Not ,if it is alphabet create a replica of it for 2 times. (take user input)

# alpha=eval(input("Enter a alphabate"))
# if alpha.isalpha():
#     print(f'{alpha*2}')
# else:
#     print(f'{alpha}')

# 19.WAP to check whether the given number value is divisible by 6 or not,if it is divisible cube that number or 
#    else perform left shift operation by 3 (take user input)

