import numpy as np

#Question 1
arr = np.array([[1, 2, 3], [5, 7, 9], [2, 4, 6], [7, 7, 7]])
def onlyOdd(arr):
    new_rows = []
    for row in arr:
        if ((row[0] % 2 == 1) and (row[1] % 2 == 1) and (row[2] % 2 == 1)):
         new_rows.append(row)  
    return new_rows

new_list = onlyOdd(arr)
print(new_list)

#Question 2
#2.1
def checkerboard():
   s = (8,8)
   checkerboard = np.zeros(s , dtype=int)
   return checkerboard

board = checkerboard()
print(board)

#2.2
import numpy as np

def checkerboard():
    s = (8,8)
    checkerboard = np.zeros((s), dtype=int)
    for row in range(8):
        if row % 2 == 1:
            for col in range(8):
                checkerboard[row, col] = (col % 2)

    return checkerboard

checkerboard = checkerboard()
print(checkerboard)

#2.3
def checkerboard():
    s = (8,8)
    checkerboard = np.zeros((s), dtype=int)
    for row in range(8):
        if row % 2 == 1:
            for col in range(8):
                checkerboard[row, col] = (col % 2)
        if row % 2 == 0:
            for col in range(8):
                checkerboard[row, col] = (1)        
    for col in range(8):
        if col % 2 == 1:
            for row in range(8):
                checkerboard[row, col] = (row % 2)
    return checkerboard

checkerboard = checkerboard()
print(checkerboard)

#2.4
def reverse_checkerboard():
    s = (8,8)
    checkerboard = np.zeros((s), dtype=int)
    for row in range(8):
        if row % 2 == 0:
            for col in range(8):
                checkerboard[row, col] = (1)
        if row % 2 == 1:
            for col in range(8):
                checkerboard[row, col] = (col % 2)
                 
    for col in range(8):
        if col % 2 == 0:
            for row in range(8):
                checkerboard[row, col] = (row % 2)
                
    for col in range(8):
        if col % 2 == 1:
            checkerboard[row, col] = (0)
            for row in range(8):
                checkerboard[row, col] = (row % 1)

    for row in range(8):
        if row % 2 == 0:
            for col in range(8):
                checkerboard[row, col] = (col % 2)
    return checkerboard

reverse_checkerboard = reverse_checkerboard()
print(reverse_checkerboard)

#3
def expansion(universe, spacing):
    space = " "
    new_space = ""
    final_array = []

    for i in range(spacing):
        new_space = new_space + space

    for word in universe:
        new_word = ""

        for letter in word:
            new_word = new_word + letter + new_space
        final_array.append(new_word)
        print_array = np.array(final_array)
    return print_array

universe = np.array(["galaxy", "clusters"])
spacing = 2
print(expansion(universe, spacing))

#4
np.random.seed(42)
planets = np.random.randint(100, 1000, (5, 5))
print("My initial array is:")
print(planets)

#The numbers different from the homewrok example possibly due to a different version of numpy being run on my computer. 
#The expected result is array([566,535,960,714,230])

def secondLargest(planets):
    my_list = np.array([])
    final_list = []
    for col in range(planets.shape[1]):
        my_list = np.empty(0)
        for row in range(planets.shape[0]):
            my_list = np.append(my_list, planets[row, col])
        final_list.append(my_list)

    second_largest_values = []
    for col in final_list:
        element_to_remove = np.max(col)
        col_without_max = np.delete(col, np.where(col == element_to_remove))
        second_largest = np.max(col_without_max)
        second_largest_values.append(second_largest)

    return second_largest_values
print(secondLargest(planets))
