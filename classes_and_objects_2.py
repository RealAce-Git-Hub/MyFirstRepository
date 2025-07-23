class Vegetable:
    def __init__(self,name=None,weight=None,color=None,taste=None,odor=None):
        self.name = name
        self.weight = weight
        self.color = color
        self.taste = taste
        self.odor = odor

    def eat(self):
        print(self.name,"can be eaten")

    def cut(self):
        print(self.name,"can be cut")

    def juice(self):
        print(self.name,"can become a juice")

    def cook(self):
        print(self.name,"can be cooked")

if __name__ == "__main__":
    kale = Vegetable("Kale",0.05,"Green","Bitter","Leafy")
    eggplant = Vegetable("Eggplant",0.4,"Purple,","Bitter","Earthy")
    carrot = Vegetable("Carrot",0.2,"Orange,","Sweet", "Fresh")

    kale.eat()
    eggplant.eat()
    carrot.eat()

    print()
    print()

    kale.cut()
    eggplant.cut()
    carrot.cut()

    print()
    print()

    kale.juice()
    eggplant.juice()
    carrot.juice()

    print()
    print()

    kale.cook()
    eggplant.cook()
    carrot.cook()