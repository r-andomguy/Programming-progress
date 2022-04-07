'''
EXERCISE LESSON 4 - DATA STRUCTURW
'''

from funcoes_list import *
# primary variables
x = []
i = 0

# inserting values to the list. (declare)
print("Fill in a list to start the program.")
list_size = int(input('Number of list elements: '))

if list_size < 0:
    error_handling_list(list_size)
else:
    skip
        

for i in range(0, list_size):
    num = float(input("Enter a number to list.\n {}º element: ".format(i)))
    i += 1
    x.append(num)

i = 0
print("\n░░░░░░░░░░░░░░░░░░░░░░░░░░\nDeclared list:\n",x, "\n░░░░░░░░░░░░░░░░░░░░░░░░░░",)
print("\nLIST MANIPULATION MENU.\nAfter declaring your list, choose one of the options to start manipulating your list.\n")

# operations menu to manipulate the list
option = int(input("1st - Insert a new element.\n2º - Remove an element from the list.\n3º - See element in the list.\n4th - Insert element based on position.\n5º Check list size.\nOption: "))

if option == 1:
    insert_n(x)
elif option == 2:
    remove_n(x,option)
elif option == 3:
    number_to_be_searched(x)
elif option == 4:
    insert_number_by_position(x)
elif option == 5:
    list_size(x)
else:
    error_handling()
