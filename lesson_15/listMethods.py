"""
List methods

These are methods that can be applied specifically to values that are of the List type.
"""


# index in this case is the method that is called. To call them on a variable, use
# the dot notation.
spam = ["hello", "hi", "howdy", "heya"]
spam.index("hello") == 0


cats = ["zophie", "pooka", "fat-tail", "pooka"]
# This gives back the first index found with the value:
cats.index("pooka") == 1

# Items can be inserted into a list at a given index:
# Doing this modifies a list in-place, it doesn't return a new object. It's reusing
# the same list as they are mutable.
cats.insert(1, "chicken")
cats[1] == "chicken"

# Instead of using the delete method which takes an index, remove can remove
# the first instance of the given value:
cats.remove("fat-tail")

# Lists can be reversed or sorted:
cats.sort(reverse=True)
# This does not sort in "true" alphabetical order, it does so in ASCII-betical order.
# In order to get Z to appear after a, use key=str.lower
cats.sort()
cats.sort(key=str.lower)
