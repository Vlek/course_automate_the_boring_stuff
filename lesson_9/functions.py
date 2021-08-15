"""

Along with built-ins, users can also define their own functions.

The definition of a function does only that, the code is only run
once it's the case that it is called later on.

Functions allow for code to only be defined once but used
multiple times throughout the code. This allows us to stay DRY
which helps reduce errors, make code easier to read, and also
easier to add to.

Functions can optionally be made to accept parameters which will
change how the function performs.

All functions have a return type, those that do not pass a return
value are returning None.

Some functions have key word arguments. Instead of the parameters
being positional, they can be given using their key.
An example being print("Hello", "world!, sep=" ")
"""

from typing import Union

def hello(name: str) -> None:
    print(f"Hello {name}")


hello("Alice")
hello("Bob")


def plusOne(number: Union[int, float]) -> Union[int, float]:
    return number + 1


assert print() == None
