#  1. A movie theatre charges different ticket prices: Children Rs.100, Adults Rs.200, Seniors
# #  Rs.150. Write a program to calculate ticket price based on age.

# age=eval(input("enter your age:"))
# if age<18:
#     print(f'your age is {age} and the ticket price is 100')
# if age>=18 and age<=59:
#       print(f'your age is {age} and the ticket price is 200')
# if age>=60:
#       print(f'your age is {age} and the ticket price is 150')

#  2. An ATM allows withdrawal only if the entered amount is a multiple of 100 and balance
#  after withdrawal does not go below Rs.500. Write a program to validate the transaction.

# balance=5000
# amount=eval(input("enter amount you want to withdraw :"))
# if amount<=balance-500:
#     print(f'you withdraw {amount}')
#     updated_balance=balance-amount
#     print(f'your remaining balance is : {updated_balance}')
# else:
#     print(f'invalid transaction')

# 3. A company gives bonus: >10 years service → 10% bonus, 6–10 years → 5% bonus, <6 years → no bonus. Accept years of service and salary, then calculate bonus.

# exp=eval(input("Enter your experience :"))
# sal=eval(input("Enter your salary :"))
# if exp>10:
#     print(f'hiked_salary {sal*1.10} as per your exp:{exp}')
# if 6<=exp<=10:
#     print(f'hiked_sal {sal*1.05} as per your exp:{exp}')
# if exp<6:
#     print(f'{sal} no hiked sal dueto less experience')

#  4. An online store offers free shipping if the cart value is above Rs.500, otherwise charges Rs.50. Write a program to calculate final amount.

# cart_amount=eval(input("enter the cart price: "))
# if cart_amount>500:
#     print(f'final bill : {cart_amount}')
# else:
#     print(f'final bill including charges : {cart_amount+50}')

#  5. A student passes if they score at least 40 in each subject and 50% overall. Accept
#  marks of 5 subjects and decide pass/fail.

# subj1=eval(input("enter marks of sub1 : "))
# subj2=eval(input("enter marks of sub2 : "))
# subj3=eval(input("enter marks of sub3 : "))
# subj4=eval(input("enter marks of sub4 : "))
# subj5=eval(input("enter marks of sub5 : "))

# if subj1>=40 and subj2>=40 and subj3>=40 and subj4>=40 and subj5>=40 and (subj1+subj2+subj3+subj4+subj5)/5>=50:
#     print(f'student is passed')
# else:
#     print('student is failde')

#  6. A railway reservation system allows senior citizens (age ≥ 60) to get 40% discount.
# #  Accept age and fare, then calculate final fare

# amount=eval(input("enter amount : "))
# age=eval(input("enter age : "))

# if age>=60:
#     print(f'total payable : {amount-amount*0.60}')
# else:
#     print(f'total payable : {amount}')

#  8. A traffic police fine system: Speed ≤60 → No fine, 61–80 → Rs.500, 81–100 →
#  Rs.2000, >100 → License Suspended. Accept speed and print result.

# speed=eval(input("enter the speed : "))
# if speed<=60:
#     print(f'No fine')
# elif 61<=speed<=80:
#     print(f'fine 500')
# elif 81<=speed<=100:
#     print(f'fine 2000')
# else:
#     print(f'fine 5000')

#  9. A gym membership: Students → 30% discount, Senior citizens → 20%, Others → No
#  discount. Write a program to calculate fee.

# fee_of_gym=1000
# age=eval(input("enter your age : "))
# if 12<=age<=22:
#     print(f'fees of the gym is : {fee_of_gym-fee_of_gym*0.30}')
# elif age>=60:
#     print(f'fees of the gym is : {fee_of_gym-fee_of_gym*0.20}')
# else:
#     print(f'fees of the gym is : {fee_of_gym}')


#  10. A water bill system: First 1000 liters → Rs.5 per 100 liters, Next 2000 liters → Rs.7 per
#  100 liters, Above 3000 liters → Rs.10 per 100 liters. Accept consumption and print bill.

# water_consumed=eval(input("enter how much water_consumed : "))
# if water_consumed<=1000:
#     print(f'water bill={water_consumed*5/100}')
# elif 1000<water_consumed<=2000:
#     print(f'water bill={water_consumed*7/100}')
# else:
#     print(f'water bill={water_consumed*10/100}')

#  11. A bank allows loans only if salary ≥ Rs.25000 and credit score ≥ 700. Accept both and
#  print eligibility.

# salary=eval(input("Enter your salary : "))
# credit_score=eval(input("Enter your credit score : "))
# if salary>=25000 and credit_score>=700:
#     print("eligible for loan")
# else:
#     print("not eligible for visa")

#  12. A shop gives discounts: On Monday → 5%, Wednesday → 10%, Friday → 20%.
#  Accept purchase amount and day, then print final bill.

# purchase_amount=eval(input("enter your purchased_amount : "))
# day=eval(input("enter day : "))
# if day=='monday':
#     print(f'total bill payable+added discount of 5% = {purchase_amount*0.95}')
# elif day=='wenesday':
#     print(f'total bill payable+added discount of 10% = {purchase_amount*0.90}')
# elif day=='friday':
#     print(f'total bill payable+added discount of 20% = {purchase_amount*0.80}')
# else:
#     print(f'total bill payable= {purchase_amount}')

#  13. A library allows borrowing only if no pending fines and membership is valid. Accept
#  both conditions and print if allowed.

# pending_fine=eval(input("enter pending fine : "))
# membership_valid = eval(input("enter membership valid (True or False):"))
# if pending_fine==0 and membership_valid=='True':
#     print(f'your allowed')
# else:
#     print(f'not allowed')

#  14. A flight check-in system: Passenger must carry ID proof; if not, boarding is denied.
#  Accept input and decide.

# id=eval(input("Do you have id (True/False) : "))
# if id==True:
#     print(f'Accept')
# else:
#     print(f'Denied')

# 15. A train booking allows only if seats are available and passenger age is ≥5. Accept both and decide.

# seat_avaible=eval(input("Enter seat availability (True/False) : "))
# age=eval(input("Enter age : "))
# if seat_avaible==True and age>=5:
#     print("Booking allowed")
# else:
#     print("Booking denied")

#  16. A restaurant offers: Orders above Rs.1000 → Free dessert, Orders above Rs.2000 →
#  Free dessert + Free drink. Accept bill and print offer

# bill=eval(input("Enter your bill : "))
# if bill>2000:
#      print("you got the free desert+free drink")
# elif bill>1000:
#       print("you got the free desert")
# else:
#       print("nothing")

# 17. A company sets appraisal: Performance ≥90 → 25% hike, 75–89 → 15%, 60–74 →
#  10%, <60 → No hike. Accept performance and salary, print revised salary.

# performence=eval(input("Enter your appracel score : "))
# salary=eval(input("Enter your sal :"))
# if performence>=90:
#     print(f'hiked sal is :{salary*1.25}')
# elif 75 <= performence <= 89:
#     print(f'hiked sal is :{salary*1.15}')
# else:
#    print(f'hiked sal is :{salary}')

#  19. A password system locks account after 3 wrong attempts. Simulate one login attempt
#  using if–else.

# password=eval(input("enter your pass"))
# password_count=3
# if password!=1234 and password_count<=3:
#     print(f'you entered the wrong password you have {password_count-1} remaining')
# else:
#     print("password is right")

#  20. An e-commerce site applies GST: Electronics 18%, Clothes 12%, Food 5%. Accept
#  product category and price, print final bill.

# category=eval(input("Enter product category : "))
# price=eval(input("Enter price of product : "))
# if category=='Electronics':
#     print(f'final bill + tax 18% : {price*1.18}')
# elif category=='Clothes':
#     print(f'final bill + tax 12% : {price*1.12}')
# elif category=='Food':
#     print(f'final bill + tax 5% : {price*1.05}')
# else:
#     print("please enter right product")


#  product category and price, print final bill.
#  21. A health app calculates BMI and classifies: <18.5 → Underweight, 18.5–24.9 →
#  Normal, 25–29.9 → Overweight, ≥30 → Obese. Accept weight and height.

weight=eval(input("Enter your weight in kg : "))
height=eval(input("Enter your height in cm : "))
bmi=weight/(height/100)*(height/10)
if bmi<=18.5:
    print("underweight")
elif 18.5<=bmi<=24.9:
    print("normal")
elif 25<=bmi<=29.9:
    print("overweight")
