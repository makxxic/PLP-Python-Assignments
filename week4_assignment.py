
def read_file_with_error_handling():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, "r") as f:
            print("File content:\n")
            print(f.read())
        modified_content=f.upper
        with open(filename2,"w") as f2:
         f2.write(modified_content)
         print(f2.read())
         print(f"File '{f2}' created successfully!")
       
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: You don’t have permission to read '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
    print("File operation completed")  

read_file_with_error_handling()
