def append_file(file1, file2):
    try:
        with open(file2, 'r') as f2:
            content = f2.read()

        with open(file1, 'a') as f1:
            f1.write(content)

        print(f"Content from '{file2}' appended to '{file1}' successfully.")
    except FileNotFoundError:
        print(f"File '{file2}' not found.")
    except IOError:
        print(f"Error reading or writing the file.")

def main():
    file1 = input("Enter the name of the first file: ")
    file2 = input("Enter the name of the second file: ")

    append_file(file1, file2)

main()
