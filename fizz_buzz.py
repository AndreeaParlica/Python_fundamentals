def fizz_buzz(number: int) -> str:
    """
    Fizz Buzz Game

    :param number: number.
    :return:
        If the number is divisible by 3, returns `fizz`.
        If the number is divisible by 5, returns `buzz`.
        If the number is divisible  by both 3 and 5, returns `fizz buzz`the correct word: `fizz`, `buzz`, `fizz buzz` or a str(number).
    """
    if number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 ==0 and number % 5 == 0:
        return "Fizz Buzz"
    else:
        return str(number)


input("Play Fizz Buzz.     Press Enter to start.")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_number = fizz_buzz(next_number)
    players_answ = input("You go: ")
    if players_answ != correct_number:
        print("You lose, the correct answer was {}.".format(correct_number))
        break
else:
    print("Well done, you reached {}.".format(next_number))



