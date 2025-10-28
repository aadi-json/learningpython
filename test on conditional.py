# str=eval(input("enter a str: "))
# if str==str[::-1]:
#     print(f"the {str} is palindrome")

# str=eval(input("enter a str: "))
# if "Python" in str:
#     print(f'Python is present in {str}')

# str=eval(input("enter a str: "))
# if str.startswith('A'):
#     print(f'{str} starts with "A"')

# str=eval(input("Enter a str : "))
# if str in 'aeiouAEIOU':
#     str2=len(str)
#     print(str2)

str=eval(input("enter a string : "))
if str.isupper():
    print(f'{str} is in uppercase')
if str.islower():
    print(f'{str} is in lowercase')
if str.islower() and str.isupper():
    print(f'{str} is mixed')