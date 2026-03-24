#task 1
name = input()
age = int(input())
print(f'Hello, {name}! You are {age} years old.')


#task 2
a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)


#task 3
temp = int(input('Enter your temperature in Celsius: '))
print(f'Your temperature in Fahrenheit is: {temp * 9/5 + 32}')


#task 4
a = 5
b = 10

a, b = b, a

print(f"a is now: {a}")
print(f"b is now: {b}")


#task 5
num = int(input('Enter your number: '))

if num % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')


#task 6
age = int(input('Enter your age: '))

if age <= 12:
    print('Child')
elif age >= 13 and age <= 17:
    print('Teen')
else:
    print('Adult')


#task 7
a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print('A is max')
elif b > a and b > c:
    print('B is max')
else:
    print('C is max')


#task 8
a = int(input('Enter first num: '))
b = int(input('Enter second num: '))
operation = input('Operation (one from +, -, *, /): ')

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/':
    print(a / b)
else:
    print('You entered uknown symbol')


#task 9
year = int(input('Enter the year: '))

if (year % 4) == 0:
    print('The year is leap')
elif (year % 100 == 0) and (year % 400 == 0):
    print('The year is leap')
else:
    print('The year is not leap')


#task 10
score = int(input('enter yout score: '))

if 90 <= score <= 100:
    print('You got A grade')
elif 75 <= score <= 89:
    print('You got B grade')
elif 50 <= score <= 74:
    print('You got C grade')
else:
    print('You got F grade')


#task 11
balance = 1000

withdraw = int(input('Enter withdrawal amount. You got 1000 now: '))

if withdraw <= balance and withdraw > 0:
    print(f'Your balance now: {balance - withdraw}')
else:
    print('Your operation denied')


#task 12
login = "admin"
password = "1234"

l = input('Enter your login: ')
p = input('Enter your password: ')

if login == l and password == p:
    print('Welcome!')
elif login != l or password != p:
    print('Your login or password is incorrect. Acsess denied')


#task 13
p = int(input('Enter your purchase amount: '))

if p >= 100000:
    print(f'Congratulations! You got discount and your final price is {p - (p * 10) / 100}')
elif p >= 5000:
    print(f'Congratulations! You got discount and your final price is {p - (p * 5) / 100}')


#task 14
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a:
    print("Triangle exists")

    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")

else:
    print("Triangle does not exist")


#task 15
color = input('Enter your color: ')

if color == 'red':
    print('Stop')
elif color == 'yellow':
    print('Wait')
elif color == 'green':
    print('Go')
else:
    print('You entered unknown color')


#task 16
num = int(input('Enter your number: '))

if num > 0:
    print('Your number is positive')
elif num < 0:
    print('Your number is negative')
elif num == 0:
    print('Your number is zero')


if num % 2 == 0:
    print('Your number is even')
else:
    print('Your number is odd')


if 1 <= num <= 100:
    print('Your number is between 1 and 100')
else:
    print('Your number is not between 1 and 100')


#task 17
a = int(input('Enter first num: '))
b = int(input('Enter second num: '))
operation = input('Operation (one from +, -, *, /, %, **,): ')

if operation == '+':
    print(a + b)
elif operation == '-':
    print(a - b)
elif operation == '*':
    print(a * b)
elif operation == '/' and b != 0:
    print(a / b)
elif operation == '%':
    print(a % b)
elif operation == '**':
    print(a ** b)
else:
    print('You entered uknown symbol or tried to divide by zero')


#task 18
password = input('Enter your password: ')

length_ok = len(password) >= 8
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)

score = sum([length_ok, has_upper, has_digit])

if score == 3:
    print('Strong')
elif score == 2:
    print('Medium')
else:
    print('Weak')


#task 19
balance = 5000

print('1. Cheack balance')
print('2. Deposit')
print('3. Withdraw')

choice = int(input('Enter your choice: '))

if choice == 1:
    print(f'Your balance is: {balance}')
elif choice == 2:
    amount = int(input('Enter deposit amount: '))
    if amount > 0:
        balance += amount
        print(f'Your new balance is: {balance}')
    else:
        print('Invalid deposit amount')
elif choice == 3:
    amount = int(input('Enter withdrawal amount: '))
    if 0 < amount <= balance:
        balance -= amount
        print(f'Your new balance is: {balance}')
    else:
        print('Invalid withdrawal amount or insufficient funds')


#task 20
num = int(input('Try to guess the secret number: '))

if num == 7:
    print('Corrrect')
elif num < 7:
    print('Too low')
else:
    print('Too high')


#task 21
score = int(input('Enter your score: '))
att = input('Enter your attendance (%): ')

if att < '60':
    print('You failed the course (')
elif 90 <= score <= 100:
    print('You got A grade')
elif 75 <= score <= 89:
    print('You got B grade')
elif 50 <= score <= 74:
    print('You got C grade')
else:
    print('You failed the course (')


#task 22
order_cost = int(input('Enter your order cost: '))
distance = int(input('Enter delivery distance (km): '))

if order_cost > 15000:
    print('Your delivery is free!')
elif distance > 5:
    delivery_cost = 200 * (distance - 5)
    print(f'Your delivery cost is: {delivery_cost}')
else:
    print('Your delivery cost is: 1000')


#task 23
salary = int(input('Enter your salary: '))
credit_history = input('Do you have good credit history? (yes/no): ')

if salary >= 200000 and credit_history == 'yes':
    print('Approved')
else: 
    print('Rejected')


#task 24
login = input('Enter your login: ')
password = input('Enter your password: ')

if login == 'admin' and password == '1234':
    print('Welcome!')
elif login != 'admin' or password != '1234':
    print('Your login or password is incorrect. You have 1 more attempt')
    login = input('Enter your login: ')
    password = input('Enter your password: ')
    if login == 'admin' and password == '1234':
        print('Welcome!')
    else:
        print('Your login or password is incorrect. Access denied')


#task 25
print('1. Add')
print('2. Subtract')
print('3. Multiply')

choice = int(input('Enter your choice: '))

if choice == 1:
    a = int(input('Enter first num: '))
    b = int(input('Enter second num: '))
    print(f'{a + b}')
elif choice == 2:
    a = int(input('Enter first num: '))
    b = int(input('Enter second num: '))
    print(f'{a - b}')
elif choice == 3:
    a = int(input('Enter first num: '))
    b = int(input('Enter second num: '))
    print(f'{a * b}')
else:
    print('You entered unknown symbol')