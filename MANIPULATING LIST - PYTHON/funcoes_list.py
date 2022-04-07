
from unittest import skip
from numpy import size

'''FUNCTIONS'''

# inserir um novo dado
def insert_n(x):
    cont = 0
    new_n = float(input("Add a new value to the list: "))
    x.append(new_n)
    resp = int(input("Do you want to add one more element? If yes, type (1). If not, type (0) to return to the menu.\n"))
    if resp == 1:
        while resp == 1:
            new_n = float(input("Add a new value to the list: "))
            cont += 1
            x.append(new_n)
            print("Declared list:\n", x, '\n')
            resp = int(input("Do you want to add one more element? If yes, type (1). If not, type (0) to return to the menu."))
    else:
        error_handling()

# remove um elemento por index
def remove_n(x, option):
    print("Declared list:\n", x)
    new_n = float(input("Indicate the element to be removed: "))

    if new_n in x:
        x.pop(new_n)
    else:
        print("Number reported {} is not on the list.".format(new_n))
    resp = int(input("Do you want to add one more element? If yes, type (1). If not, type (0) to return to the menu..\n"))
    if resp == 1:
        new_n = float(input("Indicate the element to be removed: "))
        if new_n in x:
            x.pop(new_n)
        else:
            print("Number reported {} is not on the list.".format(new_n))
        resp = int(input("Do you want to add one more element? If yes, type (1). If not, type (0) to return to the menu."))
    else:
        error_handling()

# searching a element in the list 
def number_to_be_searched(x):
    searching = int(input('You can find two types of values:\n - The index of an existing number in the list.\n - The number in a list through index.\nType (1) to find the index, or type (2) to find a number: '))

    if searching == 1:
        element = float(input('Search by element: '))
        if element in x: 
            print(x.index(' Element declared: {}. Index position: '.format(element)))
        else: 
            print('Element not found.\n')
            new_search = int(input('Would you like to search another element? Type (1) to continue, or (0) to skip to menu.'))
            if new_search == 1:
                element = int(input('Search by element: '))
            elif new_search == 0:
                error_handling()
            else: 
                new_search = int(input('Would you like to search another element? Type (1) to continue, or (0) to skip to menu.'))
    elif searching == 2:
        i = 0
        index_search = int(input('Search by index: '))
        for i in range(x):
            while i < index_search:
                i += 1
                if i == index_search:
                    print('Index position {}. Element: '.format(index_search))
                else: 
                    print('Element not found.\n')
                    new_search = int(input('Would you like to search another element? Type (1) to continue, or (0) to skip to menu.'))
                    if new_search == 1:
                        index_search= int(input('Search by index: '))
                    elif new_search == 0:
                        error_handling()
                    else: 
                        new_search = int(input('Would you like to search another element? Type (1) to continue, or (0) to skip to menu.'))

# inserir um novo dado a partir do index
def insert_number_by_position(x):
    new_n = float(input("Element to be found in the list: "))
    cont = 0
    for i in range(x):
        cont += 1
        if new_n in x:
            for index, value in enumerate(x):
                if value == new_n:
                    new_n2 = float(input("New value to index: "))
                    x[index] = new_n2
                else:
                    print("Number reported {} is not on the list.".format(new_n))

# mostrar o tamanho da lista
def list_size(x):
    size = len(x)
    print("Tamanha da lista declarada:\n", size)

# error handling
def error_handling(option):
    print("███████████████████████████████████████\nINVALID VALUE. ENTER AN OPTION TO START THE SYSTEM\n███████████████████████████████████████")
    option = int(input("1st - Insert a new element.\n2º - Remove an element from the list.\n3º - See element in the list.\n4th - Insert element based on position.\n5º Check list size.\nOption: ")) 
    while option < 1 or option > 5:
        print("███████████████████████████████████████\nINVALID VALUE. ENTER AN OPTION TO START THE SYSTEM\n███████████████████████████████████████")
        new_op = int(
            input("If you want to continue the program, type (1). To exit, type (0)."))
        if new_op == 1:
            option = int(input("1st - Insert a new element.\n2º - Remove an element from the list.\n3º - See element in the list.\n4th - Insert element based on position.\n5º Check list size.\nOption: ")) 
        else:
            print("Shutting down the system...")
            exit

# list size error
def error_handling_list():
    print('Invalid size.')
    valid_size = int(input('List size (only values above zero): '))
    while valid_size < 0:
        print('Invalid size.\n')
        valid_size = int(input('List size (only values above zero): '))
