# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

#lists are part os the collections family in python 
#creating a list
my_list = [1,2,3,4, 5]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) #5
print(type(my_list)) # <class 'listl>
print(my_list[0]) #1
print(my_list[1:4]) # [2,3, 4]
print(my_list[1:]) # [2,3, 4, 5]
print(my_list[:-1]) # [1, 2, 3, 4]
#reverse the list
print(my_list[::-1]) # [5, 4, 3, 2 , 1]
#modifying a list
my_list.append(6) # adds 6 to the end of the list
print(my_list) # [1,2,3,4,5]
#add 7 and 8 to the end of the list
my_list.extend([7,8])
print(my_list) # [1,2,3,4,5,6,7,8]

#add 9 adn 10 to the end of the list
my_list.extend([9,10])
print(my_list) # 1,2,3,4,5,6,7,8,9.10

#remove the last item
my_list.pop()
print(my_list) # 1,2,3,4,5,6,7,8,9
#remove the item at index 2
my_list.pop(2)
print(my_list) # 1,2,3,4,5,6,7,8,9
#reverse the list
my_list.reverse()
print(my_list) # [9,8,7,6,5,4,3,2,1]
my_list.remove(4)
print(my_list) # [9,8,7,6,5,3,2,1]
#remove the last item using the negative index
my_list.remove(-1)
#add more 50 more to the end of the list

new_list = list(range(12, 120))
print(new_list)

my_list.append(new_list)
print(my_list)
#my_list.extend(new_list)
# print(my_list)

new_list = list(range(120, 620))
my_list.extend(more_list)
print(len(my_list))

#my_list.extend(new_list)
# print(my_list)

#print every 3rd number
print(my_list[ : : 3])

#print every 10th number

print(my_list[ : : 10])

# remove every 3rd item in the list
del my_list[ : : 3]
print(len(my_list))
print(my_list)

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.
foods = ["pizza", "sushi", "tacos", "pasta", "ice cream"] 
# Print the second and last item.
print(foods[1])  
print(foods[-1])
# Add a new item using .append().
foods.append("burgers")
# Remove the first item using .pop(0).
foods.pop(0)
# Reverse your list using .reverse().
foods.reverse()

print(foods)
# Create a list of 3 lists (matrix), and access the middle element.





# Notes 

# #list functions 
# .append() - adds an item to the end of th elist
# .exend() - adds mulitple items to the end of the list
# .pop() - removes and returns an item at a given index 
#     (default is the last item)
# .remove() - removes the firs occurrence of a specific Value 
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list
##########################################################################################################################
#why is a list more usrful than a variable?
# a list can hold multiple values, while a variable can only hold one value at a time

cakes = ['chococlate', 'vailla', 'red velvet', 'carrot']
print(cakes)

# access the first item
print9cakes[0]) # chocolate
#access the last item 
print(cakes[-1]) # carrot
#want to chocolate cake instead of vanilla 
cakes[0] = 'strawberry'
print(cakes) # ['strawverry', 'vanilla', 'red velvet' , 'carrot' ]
#add a new cake to the end of the list
cakes.append('lemon')
print(cakes)
cakes[1] = 'chocolate'
print(cakes) 
#remove the last cake 
cakes.pop()
print(cakes) # ['strawberry' , 'chocolate' , 'red velvet'
#instert a new cake at index 2
cakes.insert92, 'funfetti')
print(cakes) # ['strawberry', 'chocolate', funfetti',


