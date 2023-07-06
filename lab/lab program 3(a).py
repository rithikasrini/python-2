def find_occurrence_and_indices(lst, num):
    positive_indices = []
    negative_indices = []
    occurrence_count = 0

    for i in range(len(lst)):
        if lst[i] == num:
            occurrence_count += 1
            positive_indices.append(i + 1)
            negative_indices.append(i - len(lst) + 1)

    return occurrence_count, positive_indices, negative_indices


def main():
    lst = list(map(int, input("Enter a list of numbers: ").split()))
    num = int(input("Enter the element to be found: "))
occurrence_count, positive_indices, negative_indices = find_occurrence_and_indices(lst, num)

    print(f"Element {num} occurs {occurrence_count} time(s) in the list.")
    print(f"Positive Index: {', '.join(map(str, positive_indices))}")
    print(f"Negative Index: {', '.join(map(str, negative_indices))}")
