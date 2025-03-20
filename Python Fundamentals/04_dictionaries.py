# 04_dictionaries.py

# Creating a Dictionary
person = {                                # Initialize a dictionary with key-value pairs
    "name": "Alice",                      # Key "name" → value "Alice"
    "age": 25,                           # Key "age" → value 25 (integer)
    "city": "New York"                    # Key "city" → value "New York"
}
print(f"Person: {person}")               # Output: Person: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing Values
print(f"Name: {person['name']}")         # Get value of key "name" → "Alice"
print(f"Age: {person['age']}")           # Get value of key "age" → 25
print(f"City: {person['city']}")         # Get value of key "city" → "New York"

# Modifying Values
person['age'] = 26                       # Update value of key "age" from 25 → 26
print(f"Modified person: {person}")      # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

# Adding Key-Value Pairs
person['email'] = "alice@example.com"    # Add new key "email" with value "alice@example.com"
print(f"Person after adding email: {person}")  # Output: Includes new "email" key

# Removing Key-Value Pairs
del person['city']                       # Delete the key "city" and its associated value
print(f"Person after removing city: {person}")  # Output: Dictionary without "city"

# Iterating Over a Dictionary
for key, value in person.items():        # Loop through each key-value pair in the dictionary
    print(f"{key}: {value}")             # Print formatted output (e.g., "name: Alice")

# Checking for a Key
if 'name' in person:                     # Check if key "name" exists in the dictionary
    print("Name is in the dictionary.")  # Executes if True (since "name" exists)
else:
    print("Name is not in the dictionary.")