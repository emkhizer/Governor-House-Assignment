# 03_if_statements.py

# Simple If Statement
age = 20                                # Assign integer 20 to variable 'age'
if age >= 18:                            # Check if age is 18 or greater
    print("You are an adult.")           # Executes if condition is True (20 >= 18 → True)
else:                                    # Optional block if condition is False
    print("You are a minor.")            # Not executed here
# Output: You are an adult.

# If-Elif-Else Statement (multi-condition check)
score = 85                               # Assign integer 85 to variable 'score'
if score >= 90:                          # First condition: check for A grade (85 >=90 → False)
    print("Grade: A")                    
elif score >= 80:                        # Second condition: check for B grade (85 >=80 → True)
    print("Grade: B")                    # Executes this block (prints "Grade: B")
elif score >= 70:                        # Skipped because a previous condition was met
    print("Grade: C")
else:                                    # Skipped
    print("Grade: F")                    
# Output: Grade: B

# Nested If Statements
temperature = 75                         # Assign integer 75 to variable 'temperature'
if temperature > 60:                     # Outer condition: check if temp >60 (75 >60 → True)
    if temperature < 80:                 # Inner condition: check if temp <80 (75 <80 → True)
        print("The weather is nice.")    # Executes inner block (prints message)
    else:                                # Inner else (not triggered here)
        print("It's too hot.")
else:                                    # Outer else (not triggered here)
    print("It's too cold.")
# Output: The weather is nice.