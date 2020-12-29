def in_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if 'string' is a palindrome, False otherwise.
    """
    backwards = string[::-1]
    return str(string).casefold() == string.casefold()
    # return string[::-1] == string


def palidrome_setence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespaces, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if 'sentence' is a palindrome, False otherwise.
    """

    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # return string[::-1].casefold() == string.casefold()
    return in_palindrome(string)


# word = input("Please enter a word to check: ")
# if palidrome_setence(word):
#     print("'{}' is a palindrome.".format(word))
# else:
#     print("'{}' is not a palindrome.".format(word))

p = in_palindrome()
s = palidrome_setence(242)