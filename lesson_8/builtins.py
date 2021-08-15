"""

python has a number of built-in functions that can be used.

However, they need to be imported first.
e.g., random's randint

These things come in modules with their own namespaces.
random.randint

The python standard library has many different modules.

Each can be imported by comma separation within one import:
import random, sys, os, math
(However, this is bad form and linters like isort will change this)

imports can also be done by moving things to the current namespace:
from math import *
(Again, this is not suggested in most cases)
"""

import sys

print("Hello")

sys.exit()

# The code below sys.exit does not get executed!
print("Goodbye")
