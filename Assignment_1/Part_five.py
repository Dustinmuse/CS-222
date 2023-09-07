def college():

    total = 8000

    print("Inital cost: " + str(total))

    for years in range(1, 6):
        total += (total * 0.03)
        print("Year: " + str(years) + "\ncost: " + str(total))
        print()

college()