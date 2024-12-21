#1
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
if a == b:
    print ("1")
elif a > b:
    print ("2")
else:
    print("3")

#2
a=int(input("Enter a number: "))
if a%2 == 0:
    print(a,"is an even number.")
else :
    print(a,"is an odd number.")

#3
a=int(input("enter a number(1-12): "))
if a==1 :
    print("january")
if a==2:
    print("february") 
if a==3:
    print("march") 
if a==4:
    print("april") 
if a==5:
    print("may")
if a==6:
    print("june")
if a==7:
    print("july") 
if a==8:
    print("august")
if a==9:
    print("september") 
if a==10:
    print("october")
if a==11:
    print("november") 
if a==12:
    print("december")
elif a>=13:
    print("Enter a valid number!")

#4
mark = int(input("Enter the marks: "))
if mark < 25:
    print("your grade is F")

elif mark >= 25 and mark < 45:
    print("your grade is E")

elif mark >=45 and mark < 50:
    print("your grade is D")

elif mark >= 50 and mark < 60:
    print("your grade is C")

elif mark >= 60 and mark <= 80:
    print("your grade is B")

elif mark > 80:
    print("your grade is A")

else:
    print("You have entered invalid mark!")

#5
num=int(input("Enter the number: "))
if (num % 7 == 0):
    print(num ,"is divisble by 7.")
else:
    print(num, "is not divisble by 7.")

#6
a = int(input("Enter 1st num:"))
b = int(input("Enter 2nd num: "))
c = (input("Enter a valid operator: "))
if c == "+":
    print(a+b)

elif c == "-":
    print(a-b)

elif c == "*":
    print(a*b)

elif c == "/":
   print(a/b)

else:
  print('Enter a valid operator!')

#7
a = int(input("Enter a number:"))
if a%5 == 0:
    print("Hello")
else:
    print("Bye")

#8
a = int(input('Enter an integer: '))
if a%3 == 0 and a%5 == 0:
    print("FizzBuzz")

elif a%5 == 0:
    print("Buzz")

elif a%3 == 0:
    print("Fizz")

else:
    print(a,"is not divisible by both 3 and 5")

#9
char = input("Enter a single character: ").lower()  #lower() --> changes the character in lowercase.
if len(char) == 1 and char.isalpha():               #isalpha ---> to ensure whether the input is alphabetic character or not.
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please take a valid single alphabetic character.")

#10
marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    grade = "A"

elif marks >= 80 and marks <= 89:
    grade = "B"

elif marks >= 70 and marks <= 79:
    grade = "C"

elif marks >= 0 and marks < 70:
    grade = "Fail"

else:
    grade = "Invalid marks entered. Please enter a value between 0 and 100."

print(f"Your grade is: {grade}")

#11
age = int(input("Enter your age: "))

if age < 13:
    category = "Child"

elif age >= 13 and age <= 19:
    category = "Teenager"

else:
    category = "Adult"

print(f"You are {category} as your age is just {age}.")

#12
char = input("Enter a character: ")
if len(char) == 1:
    if char.isupper():
        print(f"The character '{char}' is uppercase.")

    elif char.islower():
        print(f"The character '{char}' is lowercase.")

    elif char.isdigit():
        print(f"The character '{char}' is a digit.")

    else:
        print(f"The character '{char}' is neither uppercase, lowercase, nor a digit.")
else:
    print("Enter a single character.")

#13
colour = input("Enter a colour (Red/Yellow/Green): ")
if colour == "Red":
    action = "Stop" 

elif colour == "Yellow":
    action = "Get Ready" 

elif colour == "Green":
    action = "Go"

else:
    action = "You have entered an invalid colour."

print(f"Action for {colour} colour is: {action}")

#14
age = int(input("Enter your age: "))
exp = float(input("Enter your experience in your job: "))

if age > 18 and exp >= 2:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")

#15
temp = float(input("Enter the temperature in °C: "))
if temp  > 30:
    print("It's hot, stay hydrated!")

elif temp >=15 and temp <=30:
    print("Enjoy the weather!")

else:
    print("It's cold, wear warm clothes!")

#16
menu_opt = input("choose from menu oprion (Pizza, Burger, Pasta): ")

if menu_opt == "Pizza":
    print("Price of Pizza: $10")

elif menu_opt == "Burger":
    print("Price of Burger: $7")

elif menu_opt == "Pasta":
    print("Price of Pasta: $8")

else:
    print("Invalid menu choice.")

#17
height = float(input("Enter the player's height in feet: "))
if height >= 6:
    print("Selected.")
else:
    print("Not Selected.")

#18
age = int(input("Enter your age: "))
if age >= 18:
    print("Allowed")
else:
    print("Not Allowed")

#19
user_name = input("Enter your username: ")
password = input("Enter your password: ")

if user_name == "akaayush" and password == "falcon401040":
    print("Access Granted")
else:
    print("Access Denied")

#20
a = int(input("Enter the month number(1-12): "))
if a == 12 or a == 1 or a== 2:
    print("Winter")

elif 3 <= a <= 5:
    print("Spring")

elif 6 <= a <= 8:
    print("Summer")

elif 9 <= a <= 11:
    print("Autumn")

else:
    print("Invalid month number!!")

#21
salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))

if salary >= 50000 and credit_score >= 700:
    print("Eligible to take car loan")
else:
    print("Not Eligible to take car loan")

#22
a = int(input("enter a num: "))
if 1 <= a <= 100:
    print(a,"is between 1 to 100")
else:
    print(a,"is not between 1 to 100.")






