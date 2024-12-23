#1
price=float(input("Enter the price of an item: "))
if price > 1000:
    discount = (10/100)*price
    final_price = price + discount
    print(f"Final price with discount is: {final_price}")
    
elif 500 <= price <= 1000:
    discount = (5/100)*price
    final_price = price + discount
    print(f"Final price with discount is: {final_price}")
else:
    print("Invalid input!")

#2
asking_1 = input("You want (veg/non-veg): ")
if asking_1 == "veg":
    asking_2 = input("You want to eat (Salad/Pasta): ")
    print(f"{asking_2} will be brought for you right away.")

else:
    asking_3 = input("You want to eat (Chicken/Fish): ")
    print(f"{asking_3} will be brought for you right away.")

print("Thank you for visiting us!")

#3
salary = float(input("Enter your monthly salary: "))
if salary > 50000:
    classification = "high earner"

elif salary > 20000 and salary <= 50000:
    classification = "mid earner"

else:
    classification = "low earner"

print(f"Your classified as {classification} based on your income.")

#4
a=int(input("Enter a number: "))
if a % 2 == 0:
    print(f"{a} is divisible by 2.")
    if a % 5 == 0:
        print(f"{2} is divisible by 5.")
    else:
        print(f"But {2} is not divisible by 5.")
else:
    print(f"{a} is not divisible by 2")

#5
marks=float(input("Enter your marks: "))
if marks > 50:
    if marks > 90:
        print("Excellent")
    elif 51 <= marks <= 90:
        print("Good")
    else:
        print("Invalid input!")
else:
    print("Fail")

#6
a=float(input("Enter 1st num: "))
b=float(input("Enter 2nd num: "))
c=float(input("Enter 3rd num: "))
if a > b:
    if a > c:
        largest = "a"
    else:
        largest = "c"
else:
    if b > c:
        largest = "b"
    else:
        largest = "c"
print(f"The largest number is {largest}.")

#7
print("Welcome to the Forest Adventure!")
path=input("Choose a direction(left/right): ")
if path == "left":
    ask_1 = input("Choose between (explore/rest): ")
    if ask_1 == "explore":
        print("You found treasure!")
    else:
        print("You were attacked by wild animals. Game Over.")
else:
    print("You fell into a trap. Game Over.")

#8
print("Welcome to the Jungle Survival Challenge!")
ask=input("Choose (search for food/build a shelter): ")
if ask == "search for food":
    choose = input("Choose between (hunt/gather): ")
    if choose == "hunt":
        print("You were attacked by a wild animal. Game Over.!")
    else:
        print("You found enough food. You win!")
else:
    print("Your shelter collapsed in the rain. Game Over.")

#9
print("Welcome to the Space Adventure!")
ask=input("Choose between (land on Mars/fly to Jupiter): ")
if ask == "land on Mars":
    choose = input("Choose between (explore/build a case): ")
    if choose == "explore":
        print("You want alien artifacts. You Win!")
    else:
        print("You ran out of resources. Game over.")
else:
    print("Your spaceship crashed. Game over.")

#10
print("Welcome to the Haunted Castle")
ask=input("Choose between (enter the castle/run away): ")
if ask == "enter the castle":
    choose = input("Choose the colour of the door(red/green/black): ")
    if choose == "red":
        print("You entered a room full of flames. Game Over.")
    elif choose == "green":
        print("You found the treasure. You win!")
    else:
        print("You were captured by ghosts. Game Over.")
else:
    print("You escaped safely.")

#11
print("Welcome to the Underwater World")
ask=input("Choose between (dive deeper/surface): ")
if ask == "dive deeper":
    choose = input("Choose between (search for pearls/chase the fish): ")
    if choose == "search for pearls":
        print("You found a rare pearl. You win!")
    else:
        print("You got lost underwater. Game Over.")
else:
    print("You returned safely.")

#12
print("Welcome to the Pirate Ship Adventure")
ask=input("Choose between (searches for treasure/battle enemy ships): ")
if ask == "search for treasure":
    choose = input("Choose between (dig on island/explore the cave): ")
    if choose == "dig on island":
        print("You found a hidden treasure chest. You win!")
    else:
        print("You were trapped inside. Game Over.")
else:
    want_to = input("Choose between(attack/defend): ")
    if want_to == "attack":
        print("You won the battle. You Win!")
    else:
        print("You were outnumbered. Game Over.")

#13
print("Welcome to the Wizarding World")
ask=input("Choose subject (spells/potions): ")
if ask == "spells":
    choose = input("Choose between (practice magic/compete in duels): ")
    if choose == "practice magic":
        print("You mastered a powerful spell. You win!")
    else:
        print("You lost to a rival wizard. Game Over.")
else:
    ask_to = input("Choose between(brew an elixir/create poison): ")
    if ask_to == "brew an elixir":
        print("You healed a village. You Win!")
    else:
        print("Your poison backfired. Game Over.")

#14
print("Welcome to the Cybersecurity Mission")
ask=input("Choose between (trace the hacker/secure the system): ")
if ask == "trace the hacker":
    choose = input("Choose between (track their IP/decode their message): ")
    if choose == "track their IP":
        print("You caught the hacker. You win!")
    else:
        print("The message was a trap. Game Over.")
else:
    ask_to = input("Choose between(shut down the server/upgrade the firewall): ")
    if ask_to == "shut down the server":
        print("The attack was stopped. You Win!")
    else:
        print("The hacker bypassed it. Game Over.")

#15
a=int(input("Enter a num: "))
if a % 2 == 0 and a % 7 == 0:
    print("Double seven")
elif a % 7 == 0:
    print("Lucky Seven")
elif a % 2 == 0:
    print(a)
else:
    print("Invalid input!")

#16
a=int(input("Enter a num: "))
if a > 100:
    print("Big Number")
elif a >= 50 and a <= 100:
    print("Medium Number")
else:
    print("Small Number")

#17
colour=input("Enter colour(Red/Yellow/Green): ")
if colour == "Red":
    print("Stop")
elif colour == "Yellow":
    print("Slow Down")
elif colour == "Green":
    print("Go")
else:
    print("Invalid Signal")

#18
temp=float(input("Enter temperture in celsius: "))
if temp > 40:
    print("Hot")
elif temp >= 20 and temp < 40:
    print("Warm")
else:
    print("Cold")

#19
BMI= float(input("Enter a BMI value: "))
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 24.9:
    print("Normal weight")
elif 25 <= BMI < 29.9:
    print("Overweight")
else:
    print("Obesity")

#20
num1 = int(input("Enter 1st num: "))
num2 = int(input("Enter 2nd num: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}.")

elif (num1 % 2 == 0 and num2 % 2 != 0) or (num1 %2 != 0 and num2 %2 == 0):
    diff = (num1 - num2)
    if diff < 0:
        print(f"The difference of {num1} and {num2} is 7{diff}.")
    else:
        print(f"The difference of {num1} and {num2} is {diff}.")
   
else:
    prod = num1 * num2
    print(f"The product of {num1} and {num2} is {prod}.")


#21
price = float(input("Enter the price of the item: "))
if price > 1000:
    discount =(20/100)*price
    new_price = price - discount
    print(f"The new price of the item with discount is: {new_price}")

elif price >= 500 and price <= 1000:
    discount = (10/100)*price
    new_price = price - discount
    print(f"The new price of the item with discount is: {new_price}")

elif price < 500:
    print("No discount")

else:
    print("Invalid input")

#22
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
income = float(input("Enter your annual income: "))
if age >= 18 and age < 60:

    if gender == "M": 
        if income > 1000000:
            tax = 0.30 * income
        elif 500000 < income <= 1000000:
            tax = 0.20 * income
        else:
            tax = 0.10 * income

    elif gender == "F":  
        if income > 1000000:
            tax = 0.25 * income
        elif 500000 < income <= 1000000:
            tax = 0.15 * income
        else:
            tax = 0.05 * income

elif age >= 60:  
    if income > 1000000:
        tax = 0.20 * income
    else:
        tax = 0.10 * income
else:
    print("No tax is applied to you if your age is below 18.")

if tax > 0:
    print(f"Your age is {age}, your gender is {gender}, your income is {income}. So, tax according to your details is: {tax:.2f}")

# 23
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
score = float(input("Enter your academic score: "))
if age >= 18 and age <= 25:

    if gender == 'M': 
        if score >= 85:
            print("Full Scholarship")
        elif score >= 70:
            print("Partial Scholarship")
        else:
            print("No Scholarship")

    elif gender == 'F':
        if score >= 80:
            print("Full Scholarship")
        elif score >= 65:
            print("Partial Scholarship")
        else:
            print("No Scholarship")
    
    else:
        print("Invalid gender input.")
        
else:
    print("Invalid age!")

#24
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
years = float(input("Enter your experience in years: "))

if age >= 21 and age <= 35:

    if gender == 'M': 
        if years >= 5:
            role = "Senior Developer"
        else:
            role = "Junior Developer"

    elif gender == 'F':
        if years >= 85:
            role = "Senior Analyst"
        else:
            role = "Junior Analyst"
    
    else:
        print("Invalid gender input.")

elif age > 35:
    role = "Manager Role"

else:
    print("Invalid age!")

print(f"Your job role is: {role}")

#25
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
show_type = input("Enter your show type('Matinee' or 'Evening'): ")

if age < 12:
    if show_type == "Matinee":
        rate = 500
    else:
        rate = 700

elif age >= 12 and age < 60:
    if gender == 'M': 

        if show_type == "Matinee":
            rate = 800
        else:
            rate = 100

    elif gender == 'female':
        if show_type == "Matinee":
            rate = 700
        else:
            rate = 900
    else:
        print("Invalid gender input.")

else:
    rate = 600

print(f"The ticket rate for your coosen show type '{show_type}' is: Rs {rate}")

#26
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
membership_type = input("Enter your membership type('Monthly' or 'Yearly'): ")

if age >= 18 and age < 30:

    if gender == "M":
        if membership_type == "Monthly":
            cost = 50
        else:
            cost = 500

    if gender == "M":
        if membership_type == "Monthly":
            cost = 45
        else:
            cost = 450

elif age >= 30 and age <= 50:
    if membership_type == "Monthly":
        cost = 60
    else:
        cost = 600
else:
    if membership_type == "Monthly":
        cost = 40
    else:
        cost = 400  

print(f"The membership rate for your choosen type '{membership_type}' is: Rs {cost}")





    




