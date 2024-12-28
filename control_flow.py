# Control Flow Example

# If-else statement
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

# For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break statement
for num in range(10):
    if num == 5:
        break
    print(num)

# Continue statement
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)