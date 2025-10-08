def is_armstrong_number(num):
    """Checks if a given number is an Armstrong number.

    Args:
        num: The number to check.

    Returns:
        True if the number is an Armstrong number, False otherwise.
    """

    num_str = str(num)
    num_len = len(num_str)
    sum_of_digits = 0

    for digit in num_str:
        sum_of_digits += int(digit) ** num_len

    return sum_of_digits == num

# Get input from the user
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong_number(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
