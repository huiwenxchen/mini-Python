from cs50 import get_int


def main():
    # Get height from user 
    height = get_height()
    # a loop with that prints the # vertical and horiztonal
    for i in range(height):
        print(" " * (height - (i + 1)), end="")
        print("#" * (i + 1))


# Prompt User to input height and check if the value for height is within 1 and 8
def get_height():
    while True:
        height = get_int("Height: ")
        if height >= 1 and height <= 8:
            break
    return height


main()
