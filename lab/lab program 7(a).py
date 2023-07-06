def get_element_at_index(numbers, index):
    return numbers[index]

def main():
    numbers = list(map(int, input("Enter a list of numbers: ").split()))
    try:
        index = int(input("Enter an index: "))
        element = get_element_at_index(numbers, index)
        print(f"The element at index {index} is: {element}")
    except IndexError:
        print("Index is out of range!")

main()
