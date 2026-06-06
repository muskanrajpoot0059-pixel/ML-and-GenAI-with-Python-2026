#question1 
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of Rectangle =", area)

#question2
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))
SI = (P * R * T) / 100
print("Simple Interest =", SI)

#question3 
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit =", fahrenheit)

#question4
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print("Average =", average)

#question5
num = int(input("Enter a number: "))
square = num ** 2
cube = num ** 3
print("Square =", square)
print("Cube =", cube)

#question6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After Swapping:")
print("a =", a)
print("b =", b)

#question7
# Student Report Program
# Input student details
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
# Input marks of 5 subjects
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))
m4 = float(input("Enter marks of Subject 4: "))
m5 = float(input("Enter marks of Subject 5: "))
# Calculate total marks
total = m1 + m2 + m3 + m4 + m5
# Calculate percentage
percentage = total / 5
# Display report
print("\n------ STUDENT REPORT ------")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")