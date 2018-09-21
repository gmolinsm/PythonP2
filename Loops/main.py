# Some simple examples of for and while

counter = 0
while counter < 10:

    if counter == 5:
        print("This is iteration number 5")
    else:
        print("Loop number:", counter)
    counter += 1

print("\n\n\n")

for x in range(0, 3):
    print("This is iteration number", x, "of x")
    for y in range(0, 3):
        print("This is iteration number", y, "of y")

