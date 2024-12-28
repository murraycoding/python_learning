"""
Assignment 1: Python Basics
Goal: Understand how to use variables and basic data types in Python

1. Define two variables called num1 and num2 and assign them the values 10 and 20, respectively.
2. Print the sum of num1 and num2.
3. Print the difference when subtracting num1 from num2.
4. Print the product of num1 and num2.
5. Print the result of num1 divided by num2.

6. Update the values of num1 and num2 to 15 and 25, respectively but make them strings.
7. Add a type conversion to the code to make sure the variables are integers before performing the arithmetic operations.

8. (BONUS) Use the input() function to allow the user to enter the values of num1 and num2.

"""

# Code here
print("\nPlease see the results of my task:\n")
print("--------------------------------------------------")
#1. Define two variables called num1 and num2 and assign them the values 10 and 20, respectively
num1 = 10
num2 = 20

print(f"Variables defined: num1 = {num1} ; num2 = {num2}\n")

#2. Print the sum of num1 and num2.
print(f"The sum of the 2 variables: {num1} + {num2} = {num1+num2}\n")

#3. Print the difference when subtracting num1 from num2.
print(f"The difference of the 2 variables: {num2} - {num1} = {num2-num1}\n")

#4. Print the product of num1 and num2.
print(f"The product of the 2 variables: {num2} x {num1} = {num2*num1}\n")

#5. Print the result of num1 divided by num2.

print(f"The division of the 2 variables: {num1} / {num2} = {num1/num2}\n")

print("--------------------------------------------------")

#6. Update the values of num1 and num2 to 15 and 25, respectively but make them strings.

num1 = "15"
num2 = "25"

#7. Add a type conversion to the code to make sure the variables are integers before performing the arithmetic operations.

print(f"Updated variables defined: num1 = {num1} ; num2 = {num2}\n")

print(f"The sum of the 2 updated variables: {num1} + {num2} = {int(num1)+int(num2)}\n")

print(f"The difference of the 2 updated variables: {num2} - {num1} = {int(num2)-int(num1)}\n")

print(f"The product of the 2 updated variables: {num2} x {num1} = {int(num2)*int(num1)}\n")

print(f"The division of the 2 updated variables: {num1} / {num2} = {int(num1)/int(num2)}\n")

#8. (BONUS) Use the input() function to allow the user to enter the values of num1 and num2.

print("--------------------------------------------------")
print("Now all the arithmetic operations will be calculated by the numbers you enter:\n")
print("All the numbers entered must be positive numbers\n")
num1 =float(input("Please enter the first number : "))
num2 =float(input("Please enter the second number : "))

print(f"Numbers entered: num1 = {num1} ; num2 = {num2}\n")

num1 = int(round(num1,))
num2 = int(round(num2))

print(f"Numbers rounded: num1 = {num1} ; num2 = {num2}\n")

                
#print(f"Numbers entered: num1 = {num1} ; num2 = {num2}\n")
print(f"The sum of the 2 numbers entered: {num1} + {num2} = {num1+num2}\n")
print(f"The difference of the 2 numbers entered: {num2} - {num1} = {num2-num1}\n")
print(f"The product of the 2 numbers entered: {num2} x {num1} = {num2*num1}\n")
print(f"The division of the 2 numbers entered: {num1} / {num2} = {num1/num2}\n")

print("Decimals are not taken in consideration")

# Assignment completed 