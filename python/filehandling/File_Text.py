# Open a file in read mode
file = open("myfile.txt", "r")

# Open a file in write mode
file = open("myfile.txt", "w")

# Open a file in append mode
file = open("myfile.txt", "a")



# Write data to the file
file.write("Hello, World!\n")
file.write("This is some text.")


# Read the entire content of the file
content = file.read()
print(content)

# Read a single line from the file
line = file.readline()
print(line)