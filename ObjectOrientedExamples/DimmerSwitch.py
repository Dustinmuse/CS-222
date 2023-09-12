class DimmerSwitch():
    # all functions of the DimmerSwitch class
    def __init__(self): # constructor   self (in python) = this (in java)
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self): # self must be passed in 1st argument no matter what and to all functions
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self): # self must be passed in 1st argument no matter what and to all functions
        # turn the switch off
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self): # similar to a toString method in Java
        print('Switch is on?', self.switchIsOn)
        print('Brightness is:', self.brightness)

def main():
    d0 = DimmerSwitch()
    d1 = DimmerSwitch()
    d0.turnOn()
    d0.show()
    for count in range(5):
        d0.raiseLevel()
    d0.show()
    d1.show()

main()
