""" The goal here is to explore different data types in Python. """

# Basic Data Types in Python
# Integer
num = 10
print("Integer:", num)

# Float
pi = 3.14
print("Float:", pi)

# String
name = "John Doe"
print("String:", name)

# Boolean
is_true = True
print("Boolean:", is_true)

# List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)

# Tuple
coordinates = (10, 20)
print("Tuple:", coordinates)

# Dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print("Dictionary:", person)

# Set
numbers = {1, 2, 3, 4, 5}
print("Set:", numbers)

# None
value = None
print("None:", value)

# Type Conversion
# Integer to Float
num_float = float(num)
print("Integer to Float:", num_float)

# Float to Integer
pi_int = int(pi)
print("Float to Integer:", pi_int)

# Integer to String
num_str = str(num)
print("Integer to String:", num_str)

# String to Integer
str_num = int(num_str)
print("String to Integer:", str_num)

# Boolean to String
bool_str = str(is_true)
print("Boolean to String:", bool_str)

# List to Tuple
fruits_tuple = tuple(fruits)
print("List to Tuple:", fruits_tuple)

# Tuple to List
coordinates_list = list(coordinates)
print("Tuple to List:", coordinates_list)

# Dictionary to List of Keys
keys_list = list(person.keys())
print("Dictionary to List of Keys:", keys_list)

# Set to List
numbers_list = list(numbers)
print("Set to List:", numbers_list)

# None to String
value_str = str(value)
print("None to String:", value_str)

# Use the type method to check the data type of a variable
print("Type of num:", type(num))