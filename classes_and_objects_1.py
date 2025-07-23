class Fruit:
    def __init__(self,name=None,seeds=None,shape=None,color=None,taste=None,odor=None,texture=None,weight=None):
        self.name = name
        self.seeds = seeds
        self.shape = shape
        self.color = color
        self.taste = taste
        self.odor = odor
        self.texture = texture
        self.weight = weight

    def growth(self):
        print(self.name, "can grow")

    def eat(self):
        print(self.name, "can be eaten")

    def cut(self):
        print(self.name, "can be cut")

    def juice(self):
        print(self.name, "can become a juice")

    def ripe(self):
        print(self.name, "can become ripe")

if __name__ == "__main__":
    apple = Fruit("Apple", 2,"round", "Red", "Sweet", "No Odor", "Smooth", 0.2)
    orange = Fruit("Orange", 10, "round", "Orange", "Tangy", "Sweet", "Rough", 0.2)
    pear = Fruit("Pear", 4,"water_drop","green","No Smell","smooth",0.2)

    apple.growth()
    orange.growth()
    pear.growth()

    print()
    print()

    apple.eat()
    orange.eat()
    pear.eat()

    print()
    print()

    apple.cut()
    orange.cut()
    pear.cut()

    print()
    print()

    apple.juice()
    orange.juice()
    pear.juice()

    print()
    print()

    apple.ripe()
    orange.ripe()
    pear.ripe()