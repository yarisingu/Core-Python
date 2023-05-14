# Open a file in append mode
file = open("createdbypython.txt", "a")


# Open a file in write mode
file = open("createdbypython.txt", "w")

# Write data to the file
file.write("Hello, World!\n")
file.write("This is some text.")


# Open a file in read mode
file = open("createdbypython.txt", "r")
# Read the entire content of the file
content = file.read()
print(content)

# Read a single line from the file
line = file.readline()
print(line)