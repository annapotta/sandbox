# # 1 
# animals_str = "monkey bat cat dog"

# # animals_list = [] # create an empty list that youll put spliced values in - this list is the same as animals_str.split(), not ESSENTIAL
# for animal in animals_str.split(): # splice this string and convert to a list
#     print(animal) # print spliced values 
#     # animals_list.append(animal) # add spliced values to list just to show steps - not needed 
# print()

# # 2
# numbers_str = "65, 75, 32, 22"

# numbers_list = [] # empty list to be added to
# for number in numbers_str.split(", "): # for every string number in this spliced string now
#     number = int(number) # since numbers, we need to convert to int before appending bc strings cant be used for math like comparing, averaging, anything numeric ("65" + "10" would be 6510)
#     numbers_list.append(number)

# for i in range(len(numbers_list)): # diff b/w number - ELEMENT - and i - INDEX - is that the former is a list and the latter (range) is a range integer
#     print(f"{i}: {numbers_list[i]}")
# print()

# # 3
# # numbers_str = input("Input some numbers, separated by a comma: ")

# numbers_list = []
# for number_str in numbers_str.split(","):
#     if number_str == "one":
#         numbers_list.append(1)
#     elif number_str == "two":
#         numbers_list.append(2)
#     elif number_str == "three":
#         numbers_list.append(3)
#     elif number_str == "four":
#         numbers_list.append(4)
#     elif number_str == "five":
#         numbers_list.append(5)

# print(numbers_list)
# print()

# # 4
# results_str = input("Enter wins, losses, and ties: ")

# results_list = []
# for result in results_str.split():
#     if result == "W":
#         results_list.append(2)
#     elif result == "L":
#         results_list.append(1)
#     elif result == "T":
#         results_list.append(0)

# print(results_list)
# print()

# # 5
# x_str = input("Enter x-locations: ")

# x_list_number = []
# for x in x_str.split(","):
#     x_item = x.split(":")
#     x_list_number.append(int(x_item[1]))

# print(x_list_number)
# print()

# 6
dimensions = input("Enter xy coordinates: ")

dimensions_list = []

for dim in dimensions.split(" - "):
    dim_xy = dim.split(",")
    dim_x_str = dim_xy[0]
    dim_y_str = dim_xy[1]
    dim_x_split = dim_x_str.split(":")
    dim_x = dim_x_split[1]
    dim_y_split = dim_y_str.split(":")
    dim_y = dim_y_split[1]
    dimensions_list.append([int(dim_x), int(dim_y)])

print(dimensions_list)