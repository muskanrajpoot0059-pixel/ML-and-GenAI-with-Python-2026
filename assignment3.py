#question 1
#function to print first 10 natural numbers:
def print_first_10():
    for i in range(1, 11):
        print(i)

print_first_10()

#question 2 
def sum_natural(n):
    return n * (n + 1) // 2
n = 10
print("\nSum of first", n, "natural numbers =", sum_natural(n))


#question 3
#
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
num = 12345
print("\nReverse of", num, "=", reverse_number(num))
 
#question 4
#Function to count digits in a number
def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count

num = 12345
print("\nNumber of digits in", num, "=", count_digits(num))

#question 5 
# 5. Function to check palindrome number
def is_palindrome(num):
    return num == reverse_number(num)

num = 121
if is_palindrome(num):
    print("\n", num, "is a Palindrome Number")
else:
    print("\n", num, "is not a Palindrome Number")

#question 6 
## 6. Function to generate Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    print("\nFibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
fibonacci(10)

#question 7 
# 7. Calculator Using Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Division by zero not allowed"

print("\nCalculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(num1, num2))
elif choice == 2:
    print("Result =", subtract(num1, num2))
elif choice == 3:
    print("Result =", multiply(num1, num2))
elif choice == 4:
    print("Result =", divide(num1, num2))
else:
    print("Invalid Choice")

#question 8 
# Write student details to a text file

file = open("student.txt", "w")

name = input("Enter student name: ")
roll = input("Enter roll number: ")
marks = input("Enter marks: ")

file.write("Name: " + name + "\n")
file.write("Roll No: " + roll + "\n")
file.write("Marks: " + marks + "\n")

file.close()

print("Student details saved successfully.")

#question 9
# Read data from student.txt

file = open("student.txt", "r")

data = file.read()
print("File Contents:")
print(data)

file.close()

#question 10 
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid numbers.")

#question 11
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)


# Creating object
s1 = Student("Pintu", 92)

# Display details
s1.display()