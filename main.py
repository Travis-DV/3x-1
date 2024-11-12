x = input("What is the starting number\n")
i = 0

if (x.isalpha()):
    print("Not a number")
    exit()

x = int(x)

#sorry but no
if (x <= 0):
    print("Number too small")
    exit()

while (x != 1):
    i += 1;
    if (x % 2 == 0):
        x = round(x/2)
    elif (x%2 == 1):
        x = round(x*3+1)
    print(f"x: {x}, i, {i}")


