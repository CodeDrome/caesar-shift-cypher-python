import caesarshiftcypher


def main():

    """
    Creates and prints a piece of text,
    encyphers it and prints cypher text,
    then decyphers that and prints result.
    """

    print("-----------------------")
    print("| codedrome.com       |")
    print("| Caesar Shift Cypher |")
    print("-----------------------\n")

    plaintext = "The first ray of light which illumines the gloom, and converts into a dazzling brilliancy that obscurity in which the earlier history of the public career of the immortal Pickwick would appear to be involved, is derived from the perusal of the following entry in the Transactions of the Pickwick Club, which the editor of these papers feels the highest pleasure in laying before his readers, as a proof of the careful attention, indefatigable assiduity, and nice discrimination, with which his search among the multifarious documents confided to him has been conducted."

    print(plaintext)

    print("")

    try:

        cyphertext = caesarshiftcypher.encypher(plaintext, 3)

        print(cyphertext)

        print("")

        decypheredtext = caesarshiftcypher.decypher(cyphertext, 3)

        print(decypheredtext)

    except ValueError as e:

        print(e)


main()
