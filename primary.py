# name: Samaiya Howard
# date: July 27, 2021 

# -------------------- Section 1 ------------------------- #
# ------------------ List Creation ----------------------- #

print('# -------------------- Section 1 ------------------------- #')
print('Creating an Empty List' '\n')
# 1. Creating an Empty List
# --------------------------------------------------------
# Instructions
#   1. Create empty lists using the following methods.
#       a. via List Displays
#       b. via the list() function.
#   2. Print the lists.
#
# WRITE CODE BELOW
empty_list = list()
list2 = []
print(empty_list)
print(list2)

print('\n' 'Creating a Pre-Populated List' '\n')
# 2. Creating a Pre-Populated List
# ------------------------------------------------------------
# Instructions
#   1. Create the following pre-populated lists:
#       a. A list filled with 5 integers.
#       b. A list filled with 5 floats.
#       c. A list filled with 3 boolean values (True / False)
#       d. A list of three animals
#       e. A list with of 3 objects, that are all different data types.
#       f. Convert the string of the name of a star to a list via the list() function.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers = [1, 15, -4, -26, 34]
print(integers)
floats = [17.5, 89.9, 11.0, 3.14, -4.75]
print(floats)
booleans = [4 == 4.0, 7.14 != 7.14, 6.38 <= 7.38]
print(booleans)
animals = ['cat', 'owl', 'lion']
print(animals)
diff_data_types = [100, 'digits', 3.14]
print(diff_data_types)
mj = 'Michael Jackson'
star_name = list(mj)
print(star_name)

# -------------------- Section 2 ------------------------- #
# ---------------- List Modification --------------------- #
print('\n' '# -------------------- Section 2 ------------------------- #')
print('Accessing and Modifying a List' '\n')
# 1. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Replace the item at position 2 with a new number.
#       b. Floats --> Replace the item at position 4 with a new number.
#       c. Booleans --> Replace the item at position 0 with itself negated. (not)
#       d. Animals --> Replace one of the animals with a new animal.
#       e. Objects --> Replace one of the items within the list with a new one.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW
integers[2] = 44
print(integers)
floats[4] = 77.5
print(floats)
booleans[0] = not booleans[0]
print(booleans)
animals[1] = "wolf"
print(animals)
diff_data_types[2] = 2.54
print(diff_data_types)


print('\n' 'Append, Insert, and Remove' '\n')
# 2. Accessing and Modifying a List
# ------------------------------------------------------------
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Integers --> Append a new number to the list.
#       b. Floats --> Append a new float to the list.
#       c. Booleans --> Remove one of the items from the list
#       d. Animals --> Insert a new animal at the beginning of the list.
#       e. Objects --> Insert a new object at the middle of the list.
#   2. Print the lists.
#
#   1.a has been done for you.
#
# WRITE CODE BELOW

integers.append(25)
print(integers)
floats.append(9.99)
print(floats)
booleans.remove(7.14 != 7.14)
print(booleans)
animals.insert(2,'robin')
print(animals)
diff_data_types.insert(len(diff_data_types) - 1 // 2, False)
print(diff_data_types)

print('\n' 'List Concatenation' '\n')
# 3. List Concatenation
# ------------------------------------------------------------
#
# Lists like Strings can Concatenate with other Lists using the + operator. They can also be duplicated by
#   multiplying the list.
#
# Instructions
#   1. Modify the lists created in Section 1, Part 2:
#       a. Concatenate the lists holding the integers and floats together, and save the result to a new variable.
#       d. Duplicate the list holding animals 3 times, and save the result to a new variable.
#   2. Print the new lists.
#
#   Examples are below for reference
#
# WRITE CODE BELOW
example_concatenation = [1, 2, 3] + ['cat', 'dog']
example_duplication = ['cat'] * 5
print(
    '\n'
    f'example_concatenation | {example_concatenation}' '\n'
    f'example_duplication | {example_duplication}' '\n'
)

int_float_concat = integers + floats
print('integers and floats list Concatenation >>',int_float_concat)
animals_duplicated = animals * 3
print('animals duplication >>', animals_duplicated)

# -------------------- Section 3 ------------------------- #
# --------------------- Looping -------------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Looping' '\n')
# 1. Looping
# ------------------------------------------------------------
# Instructions
#   1. Create a loop that prints out the contents of the two of the lists you have already created, using the
#       methods below.
#       a. via in range()
#       b. via direct access
#
#   An example has been shown below:
#
# WRITE CODE BELOW
for i in range(len(animals)):
    print(animals[i])
for item in animals:
    print(item)

# -------------------- Section 4 ------------------------- #
# ------------------ Comprehension ----------------------- #
print('\n' '# -------------------- Section 3 ------------------------- #')
print('Dice - Statistics' '\n')

# 1. Dice - Statistics
# ------------------------------------------------------------
# Preface
#   When we roll a dice, the side it lands on is random. However, since a dice has multiple sides that are equivalent
#       in chance of falling, then we say a side has a 1/6 chance of happening, or 16.7% chance. Lets test to see if
#       that's true!
#
# 1. Create multiple for loops to run 5, 10, 100, and 1000 times.
#   a. Within the loops, roll a dice and append the roll to a list that is keeping track of all the rolls.
# 2. After the loop has finished rolling, print the number of times each face appeared, as well as the rate of
#   rate of appearance.
#
# The beginning of the loop running 5 times has been done for you. Be sure to finish it.
#
# WRITE CODE BELOW
from random import randint

rolls = []
size = 1
def dice_roll(rolls):
    for size in [5, 10, 100, 1000]:
        rolls = []
        rolls.append(randint(1,6))

    print(f'rolls | {rolls}')
    print(f'1\t| total - {rolls.count(1)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(1) / size)}')
    print(f'2\t| total - {rolls.count(2)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(2) / size)}')
    print(f'3\t| total - {rolls.count(3)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(3) / size)}')
    print(f'4\t| total - {rolls.count(4)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(4) / size)}')
    print(f'5\t| total - {rolls.count(5)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(5) / size)}')
    print(f'6\t| total - {rolls.count(6)}\t\t| rate of appearance - {"{:.2%}".format(rolls.count(6) / size)}')
dice_roll(rolls)
# finish the rest!



