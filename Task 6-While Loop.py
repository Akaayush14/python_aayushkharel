#1
while True:
    user_input = input("Enter your age or type ('stop') to quit: ")
    if user_input.lower() == "stop":
        print("Porgram is stopped.")
        break
    try: 
        age = int(user_input)    
        if age < 18:
            print("You are a minor.")
        elif age >= 18 and age <= 60:
            print("You are an adult.")
        else:
            print("You are a senior citizen.")
    except ValueError:
        print("Invalid input! Please enter a valid age or stop.")


#2
while True:
    user_input = input("Enter the name of the vehicle: ")
    if user_input.lower() != "bus":
        print("Waiting")
        continue
    else:
        print("Finally the wait is over")
        break

#3
while True:
    fruit_name = input("Enter a fruit name: ")
    if fruit_name.lower() == "apple":
        print("You got it!")
        break
    else:
        print("Try again")
        continue

#4
while True:
    guess_pass = input("Guess a password: ")
    if guess_pass.lower() == "open sesame":
        print("Access granted!")
        break
    else:
        print("Wrong password, try again.")

#5
while True:
    day_of_week = input("Enter the day of the week: ")
    if day_of_week.lower() == "sunday":
        print("Enjoy your weekend!")
        break
    else:
        print("It's not the weekend yet.")

#6
import random
num1=random.randint(1,10)
print("The random number is:",num1)
attempt = 0
while True:
    guess_num = int(input("Guess a number: "))
    attempt += 1
    if guess_num < num1:
        print("Guess higher.")
    elif guess_num > num1:
        print("Guess lower")
    else:
        print(f"It took {attempt} attempts for the user to guess the correct number.")

#7
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == "admin" and password == "1234":
        print("Login successful")
        break
    else:
        attempts += 1
        print("Invalid credentials, try again.")

if attempts == max_attempts:
    print("Too many failed attempts.")

#8
import random
while True:
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
        
    user_answer = input(f"What is {num1} * {num2}? (Enter 'exit' to quit): ")
        
    if user_answer.lower() == "exit":
        print("Thanks for playing! Goodbye!")
        break
        
    try:
        user_answer = int(user_answer)
        if user_answer == num1 * num2:
            print("Correct!")
        else:
            print("Incorrect, try again.")

    except ValueError:
        print("Please enter a valid number or 'exit' to quit.")
    
#9
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def prime_check():
    while True:
        user_input = input("Enter a number to check if it's prime (or 'exit' to quit): ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        try:
            number = int(user_input)
            
            if is_prime(number):
                print("The number is prime.")
            else:
                print("The number is not prime.")
        
        except ValueError:
            print("Invalid input! Please enter a valid number or 'exit' to quit.")
prime_check()

#10
secret_word = "python"  
while True:
    user_guess = input("Guess the secret word (or type 'quit' to exit): ").lower()
        
    if user_guess == "quit":
        print("Goodbye!")
        break
    if user_guess == secret_word:
        print("Congratulations, you guessed the word!")
        break
    else:
        print("Incorrect, try again.")

#11
count = 0  
while count < 3:
    user_input = input("Enter a name (or 'good luck' to start counting): ")
        
    if user_input.lower() == "good luck":
        count += 1
        if count == 3:
            print("You typed good luck three times!")
        else:
            print(f"You typed the same word {count} times.")
    else:
        print("You typed something else.")









        



