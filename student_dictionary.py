student_list = ["john", "jane", "joe", "jack", "zoe", "juli", "zach", "alex", "jules", "gary"]
grades_list = [67, 43, 78, 92, 97, 54, 59, 73, 84, 85]
grades_dictionary = {student_list[0]:grades_list[0], student_list[1]:grades_list[1], student_list[2]:grades_list[2], student_list[3]:grades_list[3], student_list[4]:grades_list[4], student_list[5]:grades_list[5], student_list[6]:grades_list[6], student_list[7]:grades_list[7], student_list[8]:grades_list[8], student_list[9]:grades_list[9]}
print(grades_dictionary)

for k, v in grades_dictionary.items():
    print(k, ":", v)

fruit_prices = {"lychee": 10, "apple":5, "mango":12, "pear":8, "orange":4}
print(fruit_prices.keys())
print(fruit_prices.values())
print(fruit_prices.items())

for k, v in fruit_prices.items():
    print(k, ":", v)