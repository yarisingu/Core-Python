# Create a set
sets = {1, 2, 3}

# Print the set
print(sets)

# Add an element to the set
sets.add(4)

# Print the updated set
print(sets)

# Remove an element from the set
sets.remove(2)

# Print the updated set
print(sets)

# Check if an element is in the set
if 3 in sets:
    print("3 is in the set")
else:
    print("3 is not in the set")

# Get the size of the set
size = len(sets)
print("Size of set:", size)

# Iterate over the set
for element in sets:
    print(element)
