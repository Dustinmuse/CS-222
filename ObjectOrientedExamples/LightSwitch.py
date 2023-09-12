class LightSwitch(): # light switch object
    def __init__(self): # constructor   self (in python) = this (in java)
        self.switchIsOn = False

    def turnOn(self): # self must be passed in 1st argument no matter what and to all functions
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self): # self must be passed in 1st argument no matter what and to all functions
        # turn the switch off
        self.switchIsOn = False

def main():
    l0 = LightSwitch()
    l1 = LightSwitch()
    l2 = LightSwitch()
    l2.turnOn()
    print(l0.switchIsOn) # variables are always public
    l0.turnOn()
    print(l0.switchIsOn)
    l0.turnOff()
    print(l0.switchIsOn)
    print(l1.switchIsOn)
    print(l2.switchIsOn)

main()
