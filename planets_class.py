import matplotlib.pyplot as plt
import os

class Planets:
    def __init__(self, name, diameter, distance_from_sun, satellites=None, atmosphere=None, rotation_period=None, rotation_speed=None, revolution_period=None, revolution_speed=None, fun_fact=None):
        self.name = name
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.satellites = satellites if satellites is not None else []
        self.atmosphere = atmosphere if atmosphere is not None else []
        self.rotation_period = rotation_period
        self.rotation_speed = rotation_speed
        self.revolution_period = revolution_period
        self.revolution_speed = revolution_speed
        self.fun_fact = fun_fact

if __name__ == "__main__":
    jupiter = Planets("Jupiter", 143000.00, 777000000.00, ["Metis","Adestrea","Amalethea","Thebe","Io"], ["Hydrogen","Helium"], 9.9, 12.6, 11.9, 13.07, "Jupiter has a red spot with a size 3x of Earth.")
    venus = Planets("Venus", 12000.00, 108000000.00, None, ["Carbon Dioxide", "Sulfuric Acid"], 5832, 6.52, 244.7, 35.02, "A single day on Venus is longer than its year.")
    mercury = Planets("Mercury", 1550, 58000000, None, ["Oxygen","Sodium", "Hydrogen", "Helium", "Potassium"], 1392, 10.89, 88, 47.87, "Mercury has a crater named after Dr.Suess")
    saturn = Planets("Saturn", 120500.00, 1434000000, ["Titan","Enceladus","Hyperion","Promethius","Pandora"], ["Hydrogen", "Helium"], 10.7, 9.87, 2540, 9.69, "Saturn would float in water.")
    neptune = Planets("Neptune", 49528.00, 44708000000000.00, ["Triton","Despina","Galatea","Halimede","Hippocamp"], ["Hydrogen", "Helium"], 16.11, 2.68, 1436640, 5.43, "Neptune can rain diamonds")
    mars = Planets("Mars", 6779.00, 241680000.00, ["Phobos","Deimos"], ["Carbon Dioxide","Nitrogen","Argon"], 24.62, 868, 24.6, 86870.78, "Mars has the tallest mountain in our solar system which is about 3x the height of Mount Everest")

    image_datas = os.listdir("planet_pics")
    image_datas_dir = []
    for i in image_datas:
        print("planet_pics/" + i)
        image_datas_dir.append("planet_pics/" + i)

    f, axarr = plt.subplots(2,3)
    axarr[0,0].imshow(image_datas_dir[0])
    axarr[0,1].imshow(image_datas_dir[1])
    axarr[0,2].imshow(image_datas_dir[2])
    axarr[1,0].imshow(image_datas_dir[3])
    axarr[1,1].imshow(image_datas_dir[4])
    axarr[1,2].imshow(image_datas_dir[5])