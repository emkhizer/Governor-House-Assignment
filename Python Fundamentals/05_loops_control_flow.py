# 05_loops_control_flow.py

# For Loop
for i in range(5):                      # Loop over range(5) → 0, 1, 2, 3, 4
    print(f"Number: {i}")               # Print current value of i
# Output:
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4

# While Loop
count = 0                               # Initialize variable 'count' to 0
while count < 5:                        # Loop while 'count' is less than 5
    print(f"Count: {count}")            # Print current value of 'count'
    count += 1                          # Increment 'count' by 1
# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4

# Break Statement
for i in range(10):                     # Loop over range(10) → 0, 1, 2, ..., 9
    if i == 5:                          # Check if i equals 5
        break                           # Exit the loop immediately when i is 5
    print(f"Number: {i}")               # Print current value of i
# Output:
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4

# Continue Statement
for i in range(10):                     # Loop over range(10) → 0, 1, 2, ..., 9
    if i % 2 == 0:                      # Check if i is even (divisible by 2)
        continue                        # Skip the rest of the loop for even numbers
    print(f"Odd Number: {i}")           # Print current value of i (only odd numbers)
# Output:
# Odd Number: 1
# Odd Number: 3
# Odd Number: 5
# Odd Number: 7
# Odd Number: 9

# Nested Loops
for i in range(3):                      # Outer loop: i = 0, 1, 2
    for j in range(3):                  # Inner loop: j = 0, 1, 2 for each i
        print(f"({i}, {j})")            # Print current values of i and j
# Output:
# (0, 0)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 1)
# (1, 2)
# (2, 0)
# (2, 1)
# (2, 2)