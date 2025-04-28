# my_list = ["Tshering", 5.6, True, None, 23]
# firstArrayLength = len(my_list)
# print(my_list)

# my_list.append("Dorji")
# secondArrayLength = len(my_list)
# print(my_list)

# print(firstArrayLength - secondArrayLength)

# classmates = ["Rajesh", "Karma", "Sonam", "Tshering"]
# ArrayLength = len(classmates)
# classmates.append("Kinzang")
# for index in range(ArrayLength):
#     print(classmates[index])

# name_of_animal = ["Monkey", "Dog", "Cat", "Goat"]
# length_of_array = len(name_of_animal)

# index = 0

# while index < length_of_array:
#     print(name_of_animal[index])
#     index = index + 1

generted_nmber = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
newstack = []
index = 9

while index > -1:
    newstack.append(generted_nmber[index])
    index = index - 1

print(newstack)