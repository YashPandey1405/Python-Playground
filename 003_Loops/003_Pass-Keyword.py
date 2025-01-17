# In Python, the pass keyword is used as a placeholder
# when a block of code is syntactically required but no action is needed.

# Using pass in a for loop
for i in range(5):
    if i == 2:
        pass  # Placeholder for future code
    else:
        print(f"For loop: {i}")

# Using pass in a while loop
i = 0
while i < 5:
    if i == 3:
        pass  # Placeholder for future code
    else:
        print(f"While loop: {i}")
    i += 1
