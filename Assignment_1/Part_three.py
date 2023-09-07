def odd():

    a = int(input("Enter a positive number with no decimals: "))
    b = int(input("Enter a positive number with no decimals that is bigger than the last inputted number: "))

    total = 0
    if a % 2 == 1 and a < b:
        for number in range(a, b + 1, 2):
            total += number
        print(total)
    elif a % 2 == 0 and a < b:
        for number in range(a + 1, b + 1, 2):
            total += number
        print(total)
    else:
        print("You didn't enter a positive number with no decimals or the first input was bigger than the second input")

odd()