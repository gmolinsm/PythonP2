# Net profit exercise

try:
    gross = float(input("Please enter gross salary: "))
    while True:
        children = int(input("Please enter the number of kids: "))
        if children > 0:
            break
        else:
            print("Please enter a proper number of children")
except ValueError:
    print("Please give a proper numbers")
except:
    print("Please check input")
else:

    if gross < 1000:
        tax = 0.1
    elif gross < 2000:
        tax = 0.12
    elif gross < 4000:
        tax = 0.14
    else:
        tax = 0.18

    if gross < 2000:
        tax -= 0.01 * children
    else:
        tax -= 0.005 * children

    if tax > 0:
        net = gross * (1 - tax)
    else:
        net = gross
    print("The net salary is ", net)


