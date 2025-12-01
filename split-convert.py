5.3 EXERCISES
# finding a value in a list
import random

list = []

for i in range(len(list) + 10):
    list.append(random.randrange(1, 51))

print(f"List: {list}")
user_num = int(input("Value to find: "))

for number in list:
    if number == user_num:
        print(f"{user_num} is in the list.")

# finding the largest value in a list
import random

list = []
max_number = 0

for i in range(len(list) + 10):
    list.append(random.randrange(1, 101))

for n in list: 
    if n > max_number:
        max_number = n

print(f"Array: {list}")
print(f"Biggest: {max_number}.")

# random grades
import random 

name = input("Name (first last): ")
filename = input("Filename: ")

grades = []
for i in range(5):
    grades.append(random.randrange(1, 100))

total = 0 
print("Here are your randomly-selected grades (hope you pass):")
for i in range(5):
    print(f"Grade {i + 1}: {grades[i]}")
    total += grades[i]

average = total / 5
print(f"Your average: {average}.")

if average < 50:
    print("You DID NOT PASS. FAIL!!!!")
else: 
    print("Congrats, you passed!")

# random num, count how many times appears in list
import random

list = []

for i in range(len(list) + 10):
    list.append(random.randrange(1, 51))

print(f"List: {list}") 
user_num = int(input("Value to find: "))

count = 0
for number in list:
    if number == user_num:
        print(f"{user_num} is in the list.")
        count += 1

print(f"{user_num} was found {count} times.")

# locating largest number in a list
import random

list = []
max_number = 0

for i in range(len(list) + 10):
    list.append(random.randrange(1, 101))

for n in list: 
    if n > max_number:
        max_number = n

pos = 0
for i in list:
    if i != max_number: 
        pos += 1
    else:
        break

print(f"Array: {list}")
print(f"Biggest: {max_number}.")
print(f"It is at index {pos}.")

# random num, search for a prompted integer
import random

list = []

for i in range(len(list) + 10):
    list.append(random.randrange(1, 51))

print(f"List: {list}")
user_num = int(input("Value to find: "))

for number in list: 
    if number == user_num:
        print(f"{user_num} is in the list.")
        break
    else:
        print(f"{user_num} is not in the list.")
        break

# random num, search for prompted int and locate it
import random

list = []

for i in range(len(list) + 10):
    list.append(random.randrange(1, 51))

print(f"List: {list}")
user_num = int(input("Value to find: "))

found_count = 0

for i, number in enumerate(list):
    if number == user_num:
        print(f"{user_num} is at index {i}.")
        found_count += 1

if found_count == 0: 
    print(f"{user_num} is not in the list.")

5.4 EXERCISES

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


--------------------------------------------------------

PRACTICE QUIZ SOLUTIONS

# 1. Ask the user for 1000 words using a loop
# and put them into a list. 
# The words will be entred one at a time.
words = []

for _ in range(1000):
    word = input("enter a word: ")
    words.append(word)



# 2. Given that list above, ask the user to 
# enter a word to search for in the list. 
# The program will print out the index of the first occurance of that word.

target = input("what word to look for: ")
for i in range(len(words)):
    if words[i] == target:
        print(i)
        break


# 3. Ask the user to enter numbers on a single line separated by a space.
# Split that string and create a loop that will convert each of the inputted
# numbers to an integer either replacing the string or create a new list
# to hold the integer values.
user_numbers = input("Enter numbers on one line: ")
number_strings = user_numbers.split(" ")

numbers = []
for n in number_strings:
    n = int(n)
    numbers.append(n)


# 4. Assuming that a list containing numbers already exists - the list is called numbers.
# Search the list for the index values of all the negative numbers.
# Your program should save all the index values into another list called found.

found = []
for i in range(len(numbers)):
    n = numbers[i]
    if n < 0:
        found.append(i)

SHORT ANSWERS
# practice quiz short answer
# 1. Create a list that will store the even numbers from 0–10 inclusive.
list = []
for n in range(0, 11, 2):
    list.append(n)

# 2. How does one print out the second list element in a list called friends?
friends = ["sally", 'bob']
print(friends[1])

# 3. what are two ways to print out the last element in a list called numbers?
numbers = [1, 2]
print(numbers[-1])
print(numbers[len(numbers) - 1])

# 4. Given a list called numbers containing [76, 55, 34, 24], how do you slice the list to include only the middle two?
middle_two = numbers[1:3]

# 5. Given a list called words, how do you get a slice of only the last three words?
words = ['hi']
last_three = words[-3:]
# in this negative indexing, -3 is the start point (third last), and if you omit the end, you go all the way to the end of the list
# start at the third-last word and keep going until end of list.
