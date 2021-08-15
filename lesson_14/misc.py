"""
For-loops with lists, multiple assignment, and augmented operators
"""

# These two output the same:
for i in range(4):
    print(i)

#vs

for i in [0, 1, 2, 3]:
    print(i)


# Lists can be generated from the output of range, which creates a generator usually:
# Create a list of numbers 0 - 100 that are even:
# *** Please note that this is not suggested unless needed, this is low in practice!
spam = list(range(0, 100, 2))

# If it's the case that you need the index as well as the item, iterate over the range:
# The below code works regardless of how many supplies we have
supplies = ["pens", "staplers", "flame-throwers", "binders"]
for i in range(len(supplies)):
    print(f"Index {i} in supplies is {supplies[i]}")


# Instead of having to assign multiple things out of a list one at a time, multiple assignment op:
cat = ["fat", "orange", "loud"]
size, color, disposition = cat

size == "fat"
color == "orange"


# Variables can also be swapped using this:
a = "AAA"
b = "BBB"

a, b = b, a
a == "BBB"
b == "AAA"

# Instead of doing spam = spam + 1 to increment, there's a shortcut op:
# Augmented assignment operators:
spam = 0
spam += 1
spam = spam + 1
spam == 2

