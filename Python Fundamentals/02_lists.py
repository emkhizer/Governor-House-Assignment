# 02_lists.py

# Creating a List
fruits = ["apple", "banana", "cherry"]  # Initialize a list of strings
print(f"Fruits: {fruits}")              # Output: Fruits: ['apple', 'banana', 'cherry']

# Accessing Elements
print(f"First fruit: {fruits[0]}")      # Access first element (index 0): "apple"
print(f"Last fruit: {fruits[-1]}")      # Access last element (index -1): "cherry"

# Modifying Elements
fruits[1] = "blueberry"                 # Replace element at index 1 ("banana" → "blueberry")
print(f"Modified fruits: {fruits}")     # Output: ['apple', 'blueberry', 'cherry']

# Adding Elements
fruits.append("date")                   # Add "date" to the end of the list
print(f"Fruits after appending: {fruits}")  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Removing Elements
fruits.remove("cherry")                 # Remove the first occurrence of "cherry"
print(f"Fruits after removing: {fruits}")  # Output: ['apple', 'blueberry', 'date']

# Slicing
print(f"First two fruits: {fruits[:2]}")   # Slice from start (0) to index 2 (exclusive): ['apple', 'blueberry']
print(f"Last two fruits: {fruits[-2:]}")  # Slice from index -2 to end: ['blueberry', 'date']

# Length of a List
print(f"Number of fruits: {len(fruits)}")  # Output: 3 (current list size)

# Iterating Over a List
for fruit in fruits:                     # Loop through each element in the list
    print(fruit)                         # Print each fruit on a new line