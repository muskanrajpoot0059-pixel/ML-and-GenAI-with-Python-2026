#question1 
sum = 0
for i in range(1, 11):
    sum += i
print("Sum of first 10 natural numbers =", sum)

#question2
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)

#question3
n = int(input("Enter number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c 
#question 4 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number =", a)
elif b >= a and b >= c:
    print("Largest number =", b)
else:
    print("Largest number =", c)    

#question5
# Student Result System
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")
total = 0
for i in range(1, 6):
    marks = float(input(f"Enter marks of Subject {i}: "))
    total += marks
percentage = total / 5
# Grade Calculation
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"
print("\n----- STUDENT RESULT -----")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Total Marks:", total)
print("Percentage :", percentage, "%")
print("Grade      :", grade)