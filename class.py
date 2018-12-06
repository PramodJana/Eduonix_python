class vehicle:
    wheels=4
    def __init__(self):
        print("vehicle")

    def calcVelocity(self,x):
        return (3*x+10)



class car(vehicle):
    def __init__(self):
        self.speed=10



examplecar= car()
print(examplecar.speed)
print(examplecar.calcVelocity(23))
print(examplecar.wheels)
