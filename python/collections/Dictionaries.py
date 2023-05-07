# Create a dictionary
d = {"apple": 1, "banana": 2, "cherry": 3}

# Print the dictionary
print(d)

# Access the value associated with a key
apple_value = d["apple"]
print("Value for 'apple':", apple_value)

# Update the value associated with a key
d["banana"] = 4

# Print the updated dictionary
print(d)

# Add a new key-value pair to the dictionary
d["orange"] = 5

# Print the updated dictionary
print(d)

# Remove a key-value pair from the dictionary
del d["cherry"]

# Print the updated dictionary
print(d)

# Check if a key is in the dictionary
if "banana" in d:
    print("The value for 'banana' is", d["banana"])
else:
    print("'banana' is not in the dictionary")

# Get the size of the dictionary
size = len(d)
print("Size of dictionary:", size)

# Iterate over the dictionary
for key, value in d.items():
    print(key, value)
