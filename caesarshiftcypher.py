
def encypher(plaintext, shift):

    """
    Encypher given text with given shift.
    Only letters are encyphered, all other characters are ignored.
    Encyphered text is all upper case.
    Exception raised if shift is not between 2 and 25.
    """

    if shift < 2 or shift > 25:
        raise ValueError("shift must be between 2 and 25")

    cyphertext = []

    for letter in plaintext:
        if letter.isalpha():
            encyphered_letter_ord = ord(letter.upper()) + shift
            if encyphered_letter_ord > 90:
                encyphered_letter_ord -= 26
            cyphertext.append(chr(encyphered_letter_ord))

    return "".join(cyphertext)


def decypher(cyphertext, shift):

    """
    Decyphers given text with given shift.
    Decyphered text is converted to lower case.
    Exception raised if shift is not between 2 and 25.
    """

    if shift < 2 or shift > 25:
        raise ValueError("shift must be between 2 and 25")

    plaintext = []

    for letter in cyphertext:
        decyphered_letter_ord = ord(letter) - shift
        if decyphered_letter_ord < 65:
                decyphered_letter_ord += 26
        plaintext.append(chr(decyphered_letter_ord).lower())

    return "".join(plaintext)
