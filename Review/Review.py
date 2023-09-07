def main():
    midterm = [70, 92, 100]
    try:
        print(midterm[3])
    except:
        print("Something went wrong")
    x = 2 #when this is 0 it is an error and goes to exception and skips else
    try:
        z = 10 / x
    except ZeroDivisionError:
        print("You are dividing by zero")
    except NameError:
        print("Name Error")
    else:
        print("CS 222")
    finally: #will run no matter what
        print("BSU")

main()
