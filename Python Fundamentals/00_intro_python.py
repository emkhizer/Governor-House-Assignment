# 00_intro_python.py

# Print "Hello, World!" to the console
print("Hello, World!")  # Output: Hello, World!

# Declare variables with different data types
name = "Alice"          # Assigns a string value "Alice" to variable 'name'
age = 25                # Assigns an integer value 25 to variable 'age'
height = 5.7            # Assigns a float (decimal) value 5.7 to variable 'height'
is_student = True       # Assigns a boolean (True/False) value to variable 'is_student'

# Print variables using f-strings (formatted strings)
print(f"Name: {name}")       # Output: Name: Alice (inserts 'name' into the string)
print(f"Age: {age}")         # Output: Age: 25 (inserts 'age' into the string)
print(f"Height: {height}")   # Output: Height: 5.7 (inserts 'height' into the string)
print(f"Is Student: {is_student}")  # Output: Is Student: True (inserts 'is_student')

# Basic arithmetic operations
a = 10  # Assigns integer 10 to variable 'a'
b = 5   # Assigns integer 5 to variable 'b'

# Perform calculations and print results
print(f"Sum: {a + b}")        # 10 + 5 = 15 (addition)
print(f"Difference: {a - b}") # 10 - 5 = 5 (subtraction)
print(f"Product: {a * b}")    # 10 * 5 = 50 (multiplication)
print(f"Quotient: {a / b}")   # 10 / 5 = 2.0 (float division)
print(f"Remainder: {a % b}")  # 10 % 5 = 0 (modulus operator returns remainder)