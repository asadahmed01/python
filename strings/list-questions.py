from collections import Counter

# check if list contains an element
# li = [1, 2, 3, "a", "a", "b", "c"]
# using the in operator
# print("a" in li)
# using the list.count method
# print(li.count("a"))

# ********************************
# iterate over 2 lists at the same time
# first of all zip() the lists and iterate over the zipped list which is a tuple now
# list1 = [1, 2, 3, 4]
# list2 = ["a", "b", "c"]
# for f, s in zip(list1, list2):
#     print(f, s)


# ***********************
# removing duplicates from a list
# if you are not concerned about the order of a list, convert the list to a set and
# then convert it back to a list
# li = [3, 2, 2, 1, 1, 1]
# print(list(set(li)))

# if you want to maintain order in the list then use dict.fromkeys() and pass list
# print(list(dict.fromkeys(li)))

# *******************************
# find the index of the 1st matching element
# use the .index() method
fruit = ["pear", "orange", "apple", "grapefruit", "apple", "pear"]
print(reversed(fruit))
