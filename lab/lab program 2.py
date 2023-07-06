def can_obtain_string(s1, s2):
    i = 0
    j = 0

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            j += 1
        i += 1

    return j == len(s2)

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if can_obtain_string(string1, string2):
        print("YES")
    else:
        print("NO")

main()
