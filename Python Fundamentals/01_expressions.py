# 01_expressions.py

# Arithmetic Expressions
result = 10 + 5 * 2 - 8 / 4  # Order of operations: multiplication/division first (5*2=10, 8/4=2), then addition/subtraction (10+10-2=18)
print(f"Result: {result}")    # Output: Result: 18.0 (result is a float due to division)

# Parentheses for Precedence
result = (10 + 5) * (2 - 8) / 4  # Parentheses override default precedence: (15) * (-6) / 4 = -90 / 4 = -22.5
print(f"Result with parentheses: {result}")  # Output: Result with parentheses: -22.5

# Boolean Expressions
x = 10  # Assign integer 10 to variable x
y = 5   # Assign integer 5 to variable y

# Compare x and y using relational operators
print(f"x > y: {x > y}")   # Output: x > y: True (10 is greater than 5)
print(f"x < y: {x < y}")   # Output: x < y: False (10 is not less than 5)
print(f"x == y: {x == y}") # Output: x == y: False (10 is not equal to 5)
print(f"x != y: {x != y}") # Output: x != y: True (10 is not equal to 5)