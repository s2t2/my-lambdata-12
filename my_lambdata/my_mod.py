
# my_lambdata/my_mod.py


def enlarge(n):
    """
    Param n is a number (int or float)

    Function will enlarge the number

    Returns another number (float)
    """
    return n * 100.0


# this code breaks our ability to import enlarge from other files
#
# print("HELLO")
# y = int(input("Please choose a number"))
# print(y, enlarge(y))

if __name__ == "__main__":
    # only run the code below IF this script is invoked from the command-line
    # not if it is imported from another
    print("HELLO")
    y = int(input("Please choose a number"))
    print(y, enlarge(y))
