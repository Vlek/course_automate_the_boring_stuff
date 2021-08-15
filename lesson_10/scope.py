"""
variables can live in different scopes within a program. This means
that it can be present in one area and not exist elsewhere
depending on where it was used.

When a variable within a function are created, they exist for the
lifetime of a given function call. They do not exist outside of the
call of a function and are marked for garbage collection once the function
returns.

def spam():
    eggs = 99

spam()
# This causes an error as eggs is not globally scoped!
print(eggs)

A variable that is created locally by one function cannot use the local
scoped variables in another.

def spam():
    eggs = 99
    bacon()
    # While this does not cause an error, this may not give the desired
    # value as bacon's eggs variable does not change the value of spam's.
    print(eggs)

def bacon():
    eggs = 0

Global variables can be seen from a local scope however.

def spam():
    print(eggs)

eggs = 42
spam()

Python first checks if there is a local variable, does not find one and
then looks in the global scope. Because it found one, it print it out.

Using a global variable can be done by name, but assigning a new value
to the globally scoped variable without creating a local one requires
using the global keyword first.

def spam():
    global eggs
    eggs = "Hello"
    print(eggs)

eggs = 42
spam()
print(eggs)
"""
