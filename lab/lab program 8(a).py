def read_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines[:n]:
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError:
        print(f"Error reading file '{filename}'.")

def main():
    filename = input("Enter the filename: ")
    n = int(input("Enter the number of lines to read: "))
    read_n_lines(filename, n)

main()
