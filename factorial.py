import math
#
# def factorial(num: int) -> int:
#     """
#     Factorial function.
#
#     :param num: int.
#     :return: the factorial number.
#     """
#     factorial = 1
#     if num < 0:
#         return int("Sorry, factorial doesn't exist for negative numbers")
#     else:
#         for num in range(1, num+1):
#             factorial = factorial * num
#         return num, factorial
#
#
# for number in range(36):
#     print(factorial(number))

def factorial2(num):
    """
    Factorial function calculating the factorial of a number using math module.
    :param num: int.
    :return: int.
    """
    return math.factorial(num)

for number in range(36):
    print(number, factorial2(number))

