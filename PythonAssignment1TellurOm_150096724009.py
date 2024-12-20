input_number = int(input("Enter a number: "))
if input_number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")

num=int(input("Enter a number between 1 to 7: "))
if num==1:
    print("Monday")
elif num==2:
    print("Tuesday")
elif num==3:
    print("Wednesday")
elif num==4:
    print("Thursday")
elif num==5:
    print("Friday")
elif num==6:
    print("Saturday")
elif num==7:
    print("Sunday")
else:
    print("Invalid input")

num=int(input("Enter a number between 1 to 7: "))
match num:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")

year=int(input("Enter a year: "))
if year%400==0 or (year%4==0 and year%100!=0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

marks1=int(input("Enter marks of first subject: "))
marks2=int(input("Enter marks of second subject: "))
marks3=int(input("Enter marks of third subject: "))
marks4=int(input("Enter marks of fourth subject: "))
marks5=int(input("Enter marks of fifth subject: "))
average=(marks1+marks2+marks3+marks4+marks5)/5
if average>=90:
    print("Grade: A")
elif average>=80:
    print("Grade: B")
elif average>=70:
    print("Grade: C")
elif average>=60:
    print("Grade: D")

char=input("Enter single character: ")
if len(char)!=1:
    print("Invalid input")
elif char in "aeiouAEIOU":
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

inputList = input("Enter list of numbers: ").split()
findVal=input("Enter value to find: ")
if findVal in inputList:
    print(f"{findVal} is found in the list.")
else:
    print(f"{findVal} is not found in the list.")

num=int(input("Enter a single digit number: "))
if num==0:
    print("Zero")
elif num==1:
    print("One")
elif num==2:
    print("Two")
elif num==3:
    print("Three")
elif num==4:
    print("Four")
elif num==5:
    print("Five")
elif num==6:
    print("Six")
elif num==7:
    print("Seven")
elif num==8:
    print("Eight")
elif num==9:
    print("Nine")
else:
    print("Invalid input")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

numbers1 = [num1, num2, num3]
numbers1.sort()
print("Numbers in ascending order using sort():", numbers1)

numbers2 = sorted([num1, num2, num3])
print("Numbers in ascending order using sorted():", numbers2)

numbers3 = [num1, num2, num3]
for i in range(len(numbers3)):
    for j in range(i+1, len(numbers3)):
        if numbers3[i]>numbers3[j]:
            numbers3[i], numbers3[j] = numbers3[j], numbers3[i]
print("Numbers in ascending order using for loop:", numbers3)

num=int(input("Enter a single digit number: "))
match num:
    case 0:
        print("Zero")
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case 6:
        print("Six")
    case 7:
        print("Seven")
    case 8:
        print("Eight")
    case 9:
        print("Nine")
    case _:
        print("Invalid input")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter arithmetic operator: ")
if operator=='+':
    answer=num1+num2
elif operator=='-':
    answer=num1-num2
elif operator=='*':
    answer=num1*num2
elif operator=='/':
    answer=num1/num2
elif operator=='%':
    answer=num1%num2
print(f"The result is {answer}")

val=input("Enter a character or a digit: ")
if val.isupper():
    print("Uppercase letter")
elif val.islower():
    print("Lowercase letter")
elif val.isdigit():
    print("Digit")
else:
    print("Special character")

import random
answer=random.randint(1,100)
guess=int(input("Enter your guess: "))
while guess!=answer:
    if guess<answer:
        print("Too low")
    else:
        print("Too high")
    guess=int(input("Enter your guess: "))
print("Congratulations! You guessed the number correctly.")

attempts = 0
while attempts < 5:
    name = input("Enter name: ")
    password = input("Enter password: ")
    if name == "stud" and password == "pass":
        print("Login successful!")
        break
    else:
        print("Invalid credentials. Try again.")
        attempts += 1
if attempts == 5:
    print("Maximum attempts reached.")

for i in range(15, 0, -1):
    print(i)

sum_numbers = 0
for i in range(11, 201):
    sum_numbers += i
print("Sum of numbers from 11 to 200 is:", sum_numbers)

sum1, sum2 = 0, 0
count1, count2 = 0, 0

for i in range(1, 61):
    if 5 <= i <= 15:
        sum1 += i
        count1 += 1
    elif 21 <= i <= 60:
        sum2 += i
        count2 += 1
    else:
        pass

average1 = sum1 / count1 if count1 > 0 else 0
average2 = sum2 / count2 if count2 > 0 else 0

print("Average from 5 to 15 is:", average1)
print("Average from 21 to 60 is:", average2)

for i in range(5, 31):
    if i % 2 != 0:
        print(i)

n = int(input("Enter a number to find its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is {factorial}")

number = int(input("Enter an integer: "))
sum_of_digits = sum(int(digit) for digit in str(number))
print("Sum of digits is:", sum_of_digits)

sum_even = sum(i for i in range(30, 51) if i % 2 == 0)
print("Sum of even numbers between 30 and 50 is:", sum_even)

num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(str(i) * i)

rows = int(input("Enter the number of rows: "))
for i in range(rows*2):
    if i<rows:
        print("*"*i)
    else:
        print("*"*(rows*2-i))

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(chr(64 + i) * i)  # chr(65) is 'A', chr(66) is 'B', etc.

num = int(input("Enter a number: "))
order = len(str(num))
sum_of_powers = 0
for digit in str(num):
    sum_of_powers += int(digit) ** order

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

n = int(input("Enter the number of terms: "))
fibonacci_series = []
f1, f2 = 0, 1

for i in range(n):
    fibonacci_series.append(f1)
    f1, f2 = f2, f1 + f2

print("Fibonacci series:", fibonacci_series)

num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

import array
arr=array.array('i',[1,2,3,4,5])  # Changed curly quotes to straight quotes
sum_of_array = sum(arr)
average = sum_of_array / len(arr)

print("Sum:", sum_of_array)
print("Average:", average)

import array 

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])  # 'i' indicates the type is integer

# Reverse the array by converting it to a list, reversing it, and converting back to an array
reversed_array = array.array('i', arr[::-1])  # Reverse the array

print("Reversed array:", reversed_array)

import array

# Original array with duplicates
arr = array.array('i', [1, 2, 3, 2, 4, 5, 1])  # 'i' indicates the type is integer

# Remove duplicates by converting to a set and back to an array
unique_array = array.array('i', set(arr))  # Create a new array from the set of unique elements

# Print the unique array
print("Array with duplicates removed:", unique_array.tolist())  # Convert to list for better readability

input_string = input("Enter a string: ")
reversed_string = input_string[::-1]  # Using slicing to reverse the string
print("Reversed string:", reversed_string)

input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count=0
for i in input_string:
    if i in vowels:
        count+=1
print("Number of vowels:", count)

inputVal = input("Enter a string: ")
is_palindrome = True  # Assume it is a palindrome until proven otherwise

# Check characters from start and end moving towards the center
for i in range(len(inputVal) // 2):
    if inputVal[i] != inputVal[len(inputVal) - 1 - i]:
        is_palindrome = False  # Set flag to False if a mismatch is found
        break  # No need to check further if a mismatch is found

if is_palindrome:
    print("Is palindrome")
else:
    print("Not palindrome")

val1=input("Enter a string : ")
print("String with no duplicate characters : ", str(set(val1)))

val2 = input("Enter a string: ")
unique_chars = ""
for char in val2:
    if char not in unique_chars:
        unique_chars += char
print("String with no duplicate characters:", unique_chars)

# Input string from the user
input_string = input("Enter a string: ")

# Split the string into words
words = input_string.split()

# Print words with even length
print("Even length words:")
for word in words:
    if len(word) % 2 == 0:  # Check if the length of the word is even
        print(word)

# Input string
input_string = "Python is very easy"

# Remove spaces by splitting and joining
no_spaces_string = ''.join(input_string.split())

# Print the result
print("String with spaces removed:", no_spaces_string)

# List of ASCII values
ascii_values = [65, 66, 67, 68, 69]

# Convert ASCII values to characters and join them to form a string
for value in ascii_values:
    result_string = ''.join(chr(value)) 

# Print the resulting string
print("Converted string from ASCII values:", result_string)

# Input string from the user
input_string = input("Enter a string: ")

# Print individual characters separated by '—'
formatted_string = '—'.join(input_string)

# Print the formatted string
print("Formatted string:", formatted_string)