"""
Lists

e.g. nums = [1, 2, 3]
Comma-deliminated values, either variables or literals.
"""

# List contents can be accessed via indexing:
nums = [1, 2, 3]
nums[0] == 1
nums[1] == 2


# Lists can have lists within them:
spam = [["cat", "bat"], [10, 20, 30, 40, 50]]
spam[0] == ["cat", "bat"]
spam[1] == [10, 20, 30, 40, 50]
spam[0][0] == "cat"


# Lists can be indexed from the last index going backwards:
spam = [1, 2, 3, 4, 5]
spam[-1] == 5
spam[-2] == 4


# Lists can return a slice of values instead of just one:
spam = [1,2,3,4,5,6]
spam[0:2] == [1, 2]
spam[:4] == [1, 2, 3, 4]
spam[-1:] == 6


# Strings can be indexed in the same way as lists:
spam = "Hello"
spam[0] == "H"

animals = "catdogmouse"
animals[0:3] == "cat"

# In order to remove items from a list, use del:
spam = ["one", "two", "three", "four"]
del(spam[1])
spam == ["one", "three", "four"]

# Lists and strings can be added together using the '+' sign:
'cat' + 'dog' == 'catdog'
[1,2] + [3, 4] == [1, 2, 3, 4]

# Lists can be made using the list constructor (but not suggested!)
list('hello') == ['h', 'e', 'l', 'l', 'o']

# Things can be checked to see if they are included in a list with the "in" op:
"cat" not in [1,2,3, "dog"]
"elephant" in ["dog", "cat", "snake", "elephant"]
