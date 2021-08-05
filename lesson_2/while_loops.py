# While loops video:
spam = 0
while spam < 5:
    print("Hello world")
    spam += 1

name = ""
while name != "your name":
    name = input("Please type 'your name'")
print("Thank you!")


spam = 0
while spam < 5:
    spam += 1

    # In this case, we're going to skip and not print 3
    if spam == 3:
        continue

    print(spam)
