def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    The function is used for printing a banner using a given screen
    width and `**` either side.

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :return: a banner including text, spaces and `*` in the margins.
    raises ValueError by entering a text larger then the specified width
    """
    # screen_width = 50
    if len(text) > screen_width - 4:
        raise ValueError("String {0} in larger then specified width {1}."
                         . format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)
banner_text("*", 60)
banner_text("Always look on the light side of life", 60)
banner_text("If life seems jolly rotten", 60)
banner_text("There's something you've forgotten", 60)
banner_text("And that's to laugh and smile and dance and sing", 60)
banner_text(screen_width=60)
banner_text("When you're feeling in the dumps", 60)
banner_text("Don't be silly chumps", 60)
banner_text("Just purse your lips and whistle, that's the thing", 60)
banner_text("And...Always look on the bright side of life", 60)
banner_text("*", 60)

