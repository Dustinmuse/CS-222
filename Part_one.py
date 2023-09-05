def bmis():
    height = float(input("Enter your height in inches: "))
    weight = float(input("Enter your weight in pounds: "))

    bmi = (weight * 703) / (height ** 2)

    print("BMI: " + str(bmi))

    if bmi < 18.5:
        print("You are considered to be underweight.")
    elif 18.5 <= bmi <= 25:
        print("You are considered to be optimal weight.")
    else:
        print("You are considered to be overweight.")


bmis()
