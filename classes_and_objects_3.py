class Vehicles:
    def __init__(self,name=None,weight=None,speed=None,wheels=None,passengers=None,drivers=None):
        self.name = name
        self.weight = weight
        self.speed = speed
        self.wheels = wheels
        self.passengers = passengers
        self.drivers = drivers

    def transport(self):
        print(self.name, "can transport people")
        
    def moves(self):
        print(self.name, "can move")
        
    def seats(self):
        print(self.name, "has seats")
        
    def driver(self):
        print(self.name, "needs a driver/s")

if __name__ == "__main__":
    honda_crv = Vehicles("Honda CR-V",1600,"205kph",4,4,1)
    sixteen_car_N700 = Vehicles("16-car N700 Bullet Train",645000,"180kph",128,1323,2)
    a350_900 = Vehicles("a350-900",11000,"950kph",10,325,2)

honda_crv.transport()
sixteen_car_N700.transport()
a350_900.transport()

print()
print()

honda_crv.moves()
sixteen_car_N700.moves()
a350_900.moves()

print()
print()

honda_crv.seats()
sixteen_car_N700.seats()
a350_900.seats()

print()
print()

honda_crv.driver()
sixteen_car_N700.driver()
a350_900.driver()