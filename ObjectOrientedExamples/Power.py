class Power(object):
    default_exponent = 2

    def __init__(self, exponent=default_exponent):
        self.exponent = exponent

    def of(self, x):
        return x ** self.exponent # ** means exponent (x^y)

class RealPower(Power): #inherits from the Power class (super class)

    def of(self, x): # overrides the function in the parent class (Power class)
        if isinstance(self.exponent, int) or x >= 0: # checking if the exponent is an integer and >= 0
            return x ** self.exponent
        raise ValueError(
            'Fractional powers of negative numbers are imaginary')

def main():
    number0 = Power(5) # y = 5
    print(number0.of(3)) # 3^5
    print(number0.of(2)) # 2^5
    number2 = Power()
    print(number2.of(10))
    number1 = RealPower(2) # inheritance # when it is a fraction it throws an error due to not being an integer and if x >= 0
    print(number1.of(-3.5)) # inheritance
    print(number1.of(-2))
    number3 = RealPower(1 / 2)  # inheritance # when it is a fraction it throws an error due to not being an integer and if x >= 0
    print(number3.of(2))


main()
