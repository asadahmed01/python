#list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# res = [i + j for i in list1 for j in list2]
# print(res)

#remove the empty elements from the list
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# newList = list(filter(None, list1))
# print(newList)

# list1 = [5, 20, 15, 20, 25, 50, 20]
# filtered = list(filter(lambda x:x != 20, list1))
# print(filtered)
# unpack a list
numbers = [1, 2, 3]
for index, num in enumerate(numbers):
    print(index, num)
