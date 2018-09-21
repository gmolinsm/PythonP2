base = int(input("Please input base: "))
exponent = int(input("Please give the exponent: "))

currentBase = base

for x in range(0, exponent-1):
    multiple = 0
    for y in range(0, base):
        multiple += currentBase
    currentBase = multiple
print(base, "to the power of", exponent, "equals", currentBase)

