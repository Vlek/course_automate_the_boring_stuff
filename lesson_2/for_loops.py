# For loops video:
for i in range(5):
    print(i)

# Adding all numbers 0 - 100:
total = 0
for num in range(101):
    total += num
print(total)

print("My name is")
# Range objects can also accept a step value
# This allows us to count backwards.
for i in range(5 , -1, -1):
    print(f"Jimmy Five Times {i}")
