class NegativeAgeException(Exception):
    pass

def create_student_dictionary(name, age, marks):
    student_dict = {}
    student_dict["Name"] = name
    student_dict["Age"] = age
    student_dict["Marks"] = marks
    return student_dict

def main():
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise NegativeAgeException("Age cannot be negative.")
        marks = []
        for i in range(1, 7):
            mark = float(input(f"Enter mark for subject {i}: "))
            marks.append(mark)
        student_dictionary = create_student_dictionary(name, age, marks)
        print("Student Dictionary:")
        print(student_dictionary)
except ValueError:
        print("Invalid input. Age and marks should be numeric.")
    except NegativeAgeException as e:
        print(str(e))

main()
