# available_exits = ["north", "south", "east", "west"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game Over")
#         break
# else:
#     print("aren't you glad you got out of there")

option_list = ["learn Python","learn Java","learn tango","learn programming","learn cocking"]

print("Please select one of the options: \n(1) learn python\n(2) learn Java\n(3) learn tango\n(4) learn programming \n(5) learn cooking")
choosen_opt = input("Please select your option: ")
while choosen_opt in option_list:
    if choosen_opt.casefold() == option_list[0]:
        print("you have choose the option {}".format(choosen_opt))
    elif choosen_opt.casefold() == option_list[1]:
        print("you have choose the option {}".format(choosen_opt))


    else:
        print("Please select one of the options: \n(1) learn python\n(2) learn Java\n(3) learn tango\n(4) learn programming \n(5) learn cooking")
        choosen_opt = input("Please select your option: ")


