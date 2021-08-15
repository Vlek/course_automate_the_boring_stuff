"""
lesson 11: try and except statements


the try and except statements allow one to write code that will be
able to handle exceptions and do something different when it's
the case that one occurs.
"""

from typing import Union

def divideBy(x) -> Union[int, float, None]:
    try:
        return 42 / x
    except ZeroDivisionError:
        print("Error: attempted to divide by zero")



def numCats() -> None:
    num = input("How many cats do you have?")
    try:
        if int(num) >= 4:
            print("That is a lot of cats")
        else:
            print("That is not that many cats.")
    except ValueError:
        print("You did not enter a number")


if __name__ == "__main__":
    print(divideBy(0))
    numCats()
