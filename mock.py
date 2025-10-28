# Q1. → Write a program to take a number from the user and check if it is divisible by 5.

# num=eval(input("Enter a number:"))
# if num%5==0:
#     print(f'{num} is divisble by 5')
# else:
#     print(f'{num} is not divisible by 5')

# Q2. → Write a program to take two numbers from the user and check if both numbers are even.

# num=eval(input("Enter a number:"))
# num1=eval(input("Enter a number:"))
# if num%2==0 and num1%2==0:
#     print("both the numbers are even")
# else:
#     print(f'{num},{num1} is not even numbers')

# Q3. → Write a program to take one number from the user. If the number is even, print its square, otherwise print its cube.

# num=eval(input("Enter a number:"))
# if num%2==0:
#     print(f'The square of the {num} : {num*num}')
# else:
#     print(f'The cube root of : {num*num*num}')

# Write a program to take a float input from the user. If it is greater than 10.5, print its cube root.

# num=eval(input("Enter a num:"))
# if type(num)==float and num>10.5:
#     print(f'the cube root of {num} is {num*num*num}')

# Q5. → Write a program to take a string from the user and check whether it is a palindrome or not.

# str=input("Enter a string:")
# if str==str[::-1]:
#     print(f'the plaindrome of {str} is {str[::-1]}')
    
# Q6. → Write a program to take a list of numbers from the user and check if the length of the list is odd. If yes, print the middle element.

# lst=eval(input("enter a list:"))
# if len(lst)%2==1:
#     print(f'{lst[len(lst)//2]}')

# Q7. → Write a program to take one number from the user and if it is negative, convert it into positive.

# num=eval(input("Enter a num:"))
# if num<0:
#     print(f'{num} is negative and converted into positive {abs(num)}')

# Q8. → Write a program to take a string from the user. If the string length is even, print the first half of the string.

# str=input("Enter a string:")
# if len(str)%2==0:
#     print(f'{str[0:len(str)//2:1]}')

# Q9. → Write a program to take a list from the user. If the first and last element of the list are equal, print "Valid List".

# lst=eval(input("Enter a list :"))
# if lst[0:1:1]==lst[-1:-2:-1]:
#     print("valid list")

# Q2. → Write a program to take two numbers from the user and print the larger number.

# num=eval(input("Enter a num:"))
# num2=eval(input("Enter a num:"))
# if num>num2:
#     print(f'{num} is grater')
# else:
#     print(f'{num2} is greater')

