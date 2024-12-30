#1
a="softwarica"
for i in range(1,11):  # for i in range(10)
    print(a)

#2
a=[1,2,3,4]
sum=0
for i in range(0,len(a)):  #for i in range(len(a))
    sum = sum + a[i]
print(sum)

#3
text = input("Enter a string: ")
for i in range(0,len(text)):  
    print(f"Character at index {i}: {text[i]}")

#4
list=[1,"a","c",2,3,4]
int_list=[]
for i in list:

    if isinstance(i,int):
        int_list.append(i)

print("Integers in the list: ",int_list)

#5
list=[4,5,3,2]
mul = 1
for i in range(len(list)):
    mul = mul * list[i]
print("The multiplication of each element is:",mul)

#6
num=int(input("Enter a number: "))
for i in range(1,11):
    mul = num * i
    print(num,"*",i,"=",mul)

#7
list=[1,2,'aayush',3.5]
rev_list = []
for i in list:

    rev_list.insert(0,1)

print("Reversed list: ",rev_list)

#8
list=[1,2,3,4]
new_list = []
for i in list:
    new_list.append(i+1)
print("New list: ",new_list)

#9
list=[1,2,3,4]
for i in range(len(list)):
    if i==0 or i == len(list) - 1:
        print(list[i])

#10
list=[1,2,3,4]
for i in range(len(list)):
    if i==0 or i==1 or i==len(list)-1:
        print(list[i])

#11
list=[1,2,3,4]
for i in list:
    if i == 2:
        list[i]="a"

print("Modified list is:",list)

#12
list = [1, 2, 3, 4, 5]
even_numbers = []
odd_numbers = []
for i in list:
    if i % 2 == 0:
        even_numbers.append(i)  
    else:
        odd_numbers.append(i)  
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#13
list = [1, 2, 3, "d", 4, 5, "a"]
int_type = []
str_type = []
for i in list:
    if isinstance(i,int) :
        int_type.append(i)  
    elif isinstance(i,str):
        str_type.append(i)  
print("Integer dataype elements:", int_type)
print("String datatype elements:", str_type)

#14
list=[1,2,3,4,"a","b"]
int_type = []
str_type = []
for i in list:
    if isinstance(i,int):
        int_type.append(type(i))
    elif isinstance(i,str):
        str_type.append(type(i))
print("Integer dataype elements:", int_type)
print("String datatype elements:", str_type)

#15
input_string = input("Enter a string: ")

digits_count = 0
letters_count = 0
spaces_count = 0

for char in input_string:
    if char.isdigit():
        digits_count += 1 
    elif char.isalpha():
        letters_count += 1  
    elif char.isspace():
        spaces_count += 1  

print("Number of digits:", digits_count)
print("Number of letters:", letters_count)
print("Number of spaces:", spaces_count)

#16

username = input("Enter username: ")
password = input("Enter password: ")

validity_checks = []

if len(username) < 5:
    validity_checks.append("Username must be at least 5 characters long.")
if not username.isalnum():
    validity_checks.append("Username can only contain letters and numbers.")

if len(password) < 8:
    validity_checks.append("Password must be at least 8 characters long.")
if not any(char.isupper() for char in password):
    validity_checks.append("Password must contain at least one uppercase letter.")
if not any(char.islower() for char in password):
    validity_checks.append("Password must contain at least one lowercase letter.")
if not any(char.isdigit() for char in password):
    validity_checks.append("Password must contain at least one number.")

if validity_checks:
    for check in validity_checks:
        print(f"Invalid input: {check}")
else:
    print("Username and password are valid.")

#17
num=int(input("Enter a num: "))
if num % 2 == 0:
    print("The input",num,"is even.")
else:
    print("The input",num,"is odd.") 

#18
num=int(input("Enter a num: "))
fact=1
for i in range(1,num+1):
    fact *= i
print(f"The factorial of a",{num},"is: ",{fact})

#19
for num in range(1,9):
    print("Multiplication table of",num,"is: ")
    for i in range(1, 11):  
        print(f"{num} x {i} = {num * i}")
    print()

#20
list=[1,2,3,4]
for i in range(0,2):
    print(list[i])

#21
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum = 0
for i in range(start,end+1):
    if i % 2 != 0:
        sum += i
print(f"The addition of odd number within the range is: ",{sum})

#22
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum = 0
for i in range(start,end+1):
    if i % 2 == 0:
        sum += i
print(f"The addition of even number within the range is: ",{sum})

#23
string = input("Enter a string: ")
space_count = 0
for char in string:
    if char == ' ':
        space_count += 1
print(f"The number of spaces in the given string is {space_count}.")

#24
list=[1,2,3,4]
new_list = []
for i in list:
    new_list.append(i ** 3)
print("The new list is: ",new_list)

#25
a="programming"
b= " "
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
print(b)

#26
for num in range(0,51,1):
    if num > 7:
        break
    print(num)

#27
str = input("Enter a string: ")
for i in str:
    print(i)

#28
list = ["Ram","Shyam",1,2]
for i in list:
    if isinstance(i,str):
        print(f"Hello!{i}", end = " ")

#29
list=["ram","shyam",1,2]
new_list = []
for i in list:
    new_list.append(f"Dr.{i}")
print(new_list)

#30
list = [1,2,3,4]
new_list = [ ]
for i in list:
    new_list.append(i ** 2)
print(new_list)

#31
list=[111,32,-9,-45,-17,9,85,-10]

positive_num = [ ]

for i in list:
    if i > 0:
        positive_num.append(i)

print(positive_num)

#32
#printing the elements except 3 and 6 in new_list.
list=[0,1,2,3,4,5,6]
new_list = [ ]
for i in list:
    if (i >= 0 and i < 3) or (i > 3 and i < 6):
        new_list.append(i)
print(new_list)

#or
#printing the element only except 3 and 6.
list=[0,1,2,3,4,5,6]
for i in list:
    if i == 3 or i == 6:
        continue
    print(i)

#33
list=[1,"aayush",2.3]
new_list = [ ]
for i in list:
    new_list.append(type(i))
print(new_list)

#34
for i in range(5):
    print(i)
else:
    print("Done")

#35
for i in range(105,0,-7):
    print(i)

#36
bad_chars = [';', ':', '!', '*']
string = "py;th* o:n ! ;py * t*h:o !n"

for char in bad_chars:
    string = string.replace(char, "")

string = string.replace(" ", "")

print(string)

#37
start=int(input("Enter starting point: "))
end=int(input("Enter ending point: "))

even_count = 0
odd_count = 0

for num in range(start,end):
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")

#38
sum = 0
for num in range(3,100):
    if num % 3 == 0 or num % 5 == 0:
        sum += num
print("Sum of all multiples of 3 or 5 from range 3 to 99 is: ",sum)

#39
sum_even = 0
sum_odd = 0
for num in range(1,101):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
print("Sum of even numbers from 1 to 100 is: ",sum_even)
print("Sum of odd numbers from 1 to 100 is: ",sum_odd)

#40
palindrome = input("Enter a number: ")
if palindrome == palindrome[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

#41
number = int(input("Enter a number: "))

num_str = str(number)
num_digits = len(num_str)

sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

#42
str = input("Enter a string: ")
vowel = "aeiouAEIOU"
result = " "
for char in str:
    if char not in vowel:
        result += char

print(result)

#43
number = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")

#44

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

common_numbers = list(set(a) & set(b))

print("Common numbers:", common_numbers)

#45
number = int(input("Enter a number: "))
if number < 2:
    print(f"{number} is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")








    

















        

  
              







