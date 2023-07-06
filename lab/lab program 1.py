def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def count_digits(n):
    return len(str(n))

def main():
    num = int(input("Enter an integer: "))

    if num % 2 == 1:  # Odd number
        fact = factorial(num)
        digit_count = count_digits(fact)
        print(f"The factorial of {num} is: {fact}")
        print(f"The number of digits in the factorial is: {digit_count}")
    else:  # Even number
        if is_palindrome(num):
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")

main()
This code defines three helper functions: factorial() to calculate the factorial of a number, is_palindrome() to check if a number is a palindrome,







