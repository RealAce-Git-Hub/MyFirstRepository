class Animal:
    def __init__(self):
        #defining characteristics of Animal
        self.legs = 4
        self.ears = 2
        self.eyes = 2
        self.name = " "

    def sound(self, s = None):
        if s == None:
         print("It doesen't make a sound")

        else:
            print("It makes a sound", s)
    
    def move(self, m = None):
        if m == None:
          print("It doesen't move")
        else: 
           print("It", m)

    def assign_name(self, n = None):
        if n == None:
          print("It doesen't have a name")
        else: 
           print("It's name is", n)


if __name__ == "__main__":
    Dog = Animal()
    Cat = Animal()

    Dog.sound("Woof")
    Cat.sound("Meow")

    Dog.move("runs and jumps")
    Cat.move("runs and jumps")

    Dog.assign_name("Biscuit")
    Cat.assign_name("Snowball")

    Dog.print_name()
    Cat.print_name()