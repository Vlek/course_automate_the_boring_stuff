"""
Print a box (with optional text) given a height and width.
"""


def boxPrint(height: int = 1,
             width: int = 1,
             msg: str = "",
             wallChar: str = "*") -> None:
    """Prints a box with given text in the size width/height"""

    # Print top
    print(wallChar * width)

    for row in range(height - 2):

        # Print each row
        print(wallChar + " " * (width - 2) + wallChar)

    # Print bottom
    print(wallChar * width)


if __name__ == "__main__":
    boxPrint(5, 15)
