my_list = []  # create an empty list called my_list
#Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)  
my_list.append(40)
my_list.insert(1, 15) # Insert 15 at the second position in the list
my_list.extend([50, 60,70])  # Extend list with another list
# Remove last element
my_list.pop()
my_list.sort()  # Sort the list in ascending order
index_of_30 = my_list.index(30)  # Find index of 30
# print index of 30
print("Index of 30:", index_of_30)  # Output: Index of 30: 3


