def is_ascending(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True


def main():
    n = int(input("Enter the number of elements in the list: "))
    lst = []

    for _ in range(n):
        num = int(input("Enter the value: "))
        lst.append(num)

    if is_ascending(lst):
        print("Yes, the list is in ascending order.")
    else:
        print("No, the list is not in ascending order.")


main()



