#1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, rollno, stream):
        super().__init__(name, age)
        self.rollno = rollno
        self.stream = stream

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}, Stream: {self.stream}")

# Create an object of the Student class
student = Student("John Doe", 20, "S123", "Computer Science")
student.display()

#2
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())

#3
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 0))

#4
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(self.items.values())

cart = ShoppingCart()
cart.add_item("Apple", 1.5)
cart.add_item("Banana", 1.0)
print("Total Price:", cart.total_price())
cart.remove_item("Apple")
print("Total Price after removing Apple:", cart.total_price())

#5
class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = (overtime * (self.emp_salary / 50))
            return self.emp_salary + overtime_amount
        return self.emp_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Name: {self.emp_name}, ID: {self.emp_id}, Salary: {self.emp_salary}, Department: {self.emp_department}")

emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp1.print_employee_details()
emp1.emp_assign_department("HR")
emp1.print_employee_details()
print("Salary after working 60 hours:", emp1.calculate_emp_salary(60))

#6
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0, date_of_opening=None):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def check_balance(self):
        return self.balance

account = BankAccount("123456", "John Doe", 1000)
print("Balance after deposit:", account.deposit(500))
print("Balance after withdrawal:", account.withdraw(300))
print("Current Balance:", account.check_balance())

#7
class Shape:
    def __init__(self, colour):
        self.colour = colour

class Circle(Shape):
    def __init__(self, radius, colour):
        super().__init__(colour)
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height, colour):
        super().__init__(colour)
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height, colour):
        super().__init__(colour)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

circle = Circle(5, "Red")
rectangle = Rectangle(4, 5, "Blue")
triangle = Triangle(4, 3, "Green")

print("Circle Area:", circle.calculate_area())
print("Rectangle Area:", rectangle.calculate_area())
print("Triangle Area:", triangle.calculate_area())

#8
def count_words_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

print("Number of words:", count_words_in_file('./sample.txt'))
   
#9
with open('output.txt', 'w') as file:
    file.write("Happy Programming")

with open('output.txt', 'r') as file:
    content = file.read()
    print(content)

#10
with open('sample.txt', 'r') as file:
    print(file.read())        # i) read()
    file.seek(0)              # Reset file pointer
    print(file.read(5))       # ii) read(n)
    file.seek(0)              # Reset file pointer
    print(file.readline())     # iii) readline()
    file.seek(0)              # Reset file pointer
    print(file.readlines())    # iv) readlines()

#11
with open('output.txt', 'w') as file:
    file.write("Hello World")  # i) write()
    file.writelines(["Line 1\n", "Line 2\n"])  # ii) writelines()

#12
def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        for _ in range(n):
            print(file.readline().strip())

read_first_n_lines('sample.txt', 3)

#13
with open('output.txt', 'a') as file:
    file.write("\nAppending this line.")

with open('output.txt', 'r') as file:
    print(file.read())

#14
def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line.strip())

read_last_n_lines('sample.txt', 3)

#15
def read_file_to_list(filename):
    with open(filename, 'r') as file:
        return file.readlines()

lines = read_file_to_list('sample.txt')
print(lines)

#16
try:
    print("Trying to divide by zero...")
    result = 10 / 0
except ZeroDivisionError:
    print("Caught a division by zero error!")
finally:
    print("This will always execute.")

#17
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")

#18
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("That's not a valid integer!")

#19
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("That's not a valid integer!")
else:
    print("Result:", result)

#20
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except (ZeroDivisionError, ValueError) as e:
    print(f"Error occurred: {e}")

#21
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

#22
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

#23
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))
print("Evens:", evens)
print("Odds:", odds)

#24
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
cubes = list(map(lambda x: x ** 3, numbers))
print("Squares:", squares)
print("Cubes:", cubes)

#25
add_15 = lambda x: x + 15
print(add_15(10))

#26
multiply = lambda x, y: x * y
print(multiply(5, 3))
