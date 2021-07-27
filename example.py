# Creating an empty list
list1 = []
list2 = list()  # calling the list function
print(list1)
print(list2)

# Creating a pre-populated list
list3 = ['cat', 'dog', 'pangolin']
list4 = [100, 23, 4.3, 23.23]
list5 = [100, 'dog', 123.343, 'dolphin']
print(list3)
print(list4)
print(list5)
print(list3[0])
print(list3[1])
print(list3[2])
# print(list3[3]) # out of bounds

# You can have whatever type you want in a list, and it does not have to be
#   consistent (the items don't have to be the same type)

list1 = [
    'cat', 'dog', 'pangolin', 'panda', 'koala', 'penguin', 'cow',
    'zebra', 'manta-ray', 'elephants', 'hippo'
]
print(list1[0:3])
print(list1[4:8])
print(list1[3:9:2])

# We are allowed to slice a list just like a string, and slicing a list
#   returns the elements of the list starting at position start, and ending at
#   position stop. The return type is a list.

text1 = 'hello my dear friend'

for i in range(len(text1)):  # in range()
    print(text1[i])

print()

for char in text1:  # direct access
    print(char)

print()
# Using a for loop with lists

for i in range(len(list1)):  # in range()
    print(list1[i])

print()

for item in list1:  # direct access
    print(item)

# reassignment of an item in a list
# changing individual items within a list
print(list1)

list1[1] = 'parakeet'
print(list1)

list1[3] = 'dove'
print(list1)


# When saving a copy of a list, you do not simply want to write
# list1 = list2
# because this saves the same list to both variables.
# Instead, you want to save an explicit copy.
print()
list2 = list1[:]  # This will return a copy of the list, but not the list itself

print(list1)
print(list2)

list1[2] = 'robin'

print(list1)
print(list2)

# list.append(item)
# append --> appends the item to the end of the list

print()

list1 = []
print(list1)

# append an animal to list1
list1.append('bear')
print(list1)

list1.append('kangaroo')
print(list1)

list1.append('owl')
print(list1)

# append --> appEND --> append happens at the end
# This is the main way we add items to a list.

# list.insert(position, item)
# This is very similar to append, except instead of appending to the end,
#   we insert the item at the position given.

# Insert 'rat' to the beginning of the list
list1.insert(0, 'rat')
print(list1)

# Insert 'lion' in between 'bear' and 'kangaroo'
list1.insert(2, 'lion')
print(list1)

# When we insert to a list, we take that position and everything else
#   (at the position and to the right) is shifted one position over.

# Insert 'tanuki' in between 'kangaroo' and 'owl'
list1.insert(4, 'tanuki')
print(list1)

# Insert 'pig' to the end of the list
list1.insert(6, 'pig')
print(list1)

# You should never insert items to the end of your list.
# You should always use append in that situation.


# list.remove(element)
# Removes the first occurrence of the element in the list.
# Let's remove 'rat'
list1.remove('rat')
print(list1)

list2 = [5, 4, 1, 5, 6, 7, 3, 5, 3, 2, 6, 6, 9, 2, 1, 4, 5, 7, 4, 2, 6]
print(list2)
# Lets remove every single 2 from the list
# Lets remove 2 from the list

list2.remove(2)
print(list2)

# Lets write a loop to remove every 6 from the list
for i in range(list2.count(6)):
    list2.remove(6)

print(list2)
