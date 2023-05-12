def create_file(file_path):
    try:
        with open(file_path, "x"):
            print("File created successfully.")
    except FileExistsError:
        print("File already exists.")

# Call the function to create a file in a specific location
create_file("C:\\Users\\yaris\\OneDrive\\Desktop\\deleteafteruse\\python\\files_create_with_python_code\\createdbypython.txt")
