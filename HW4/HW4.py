twentynumlist = []
i = 0
while i < 21:
    twentynumlist.append(i)
    i = i + 1

'''
I tried to return the function with "return twentynumlist." I received this error: "return" can be used only within a function Pylance.
I qucikly realized that I had not defined a function, so I had no need for the "return" command.
'''

print(twentynumlist)

def squarelist(twentynumlist):
    squaredlist = []
    for num in twentynumlist:
        squaredlist.append(num**2)
    return squaredlist

squaringlist = squarelist(twentynumlist)
print(squaringlist)

first_fifteen_elemenets = squaringlist[0:15:1]
print(first_fifteen_elemenets)

every_fifth_element = squaringlist[4::5]
print(every_fifth_element)

sliced_last_three = squaringlist[0:18]
fancy_function = sliced_last_three[-3::-3] 
'''
Homework answer looks like [400, 289, 196, 121, 64, 25, 4],
but when the last three elements in the list are sliced, the 400 is not included. 
My answer includes every 3rd number after the three have been sliced, so it should look like [225, 144, 81, 36, 9, 0]
'''
print(fancy_function)

twenty_five_list = []
temp_list = []
def create_2d_list():
    for num in range(0,5):
        temp_list = []
        n = num
        for number in range(5*n,(5*n)+6):
            temp_list.append(number)
        temp_list.pop(0)
        twenty_five_list.append(temp_list)
        # print(twenty_five_list)
        # I ran into an error where my temp list would not clear, so my twenty_five_list only dislayed 5 lists each from 1 - 25.
        # I implemented this print statement to see what was going on it the code, and resolved the issue by adding temp_list = [] in line 42.
        # I also learned that python adds a # automatically if you press enter to break your comment into multiple lines.
    return twenty_five_list

matrix = create_2d_list()
print(matrix)

def modified_2d_list(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): 
            if matrix[i][j] % 3 == 0:
                matrix [i][j] = "?"
    return(matrix)

modified_matrix = modified_2d_list(matrix)
print(modified_matrix)

def sum_non_question_elements(modified_matrix):
    sum = 0
    for i in range(len(modified_matrix)):
        for j in range(len(modified_matrix[i])):
                if modified_matrix[i][j] != "?":
                    sum += modified_matrix[i][j]
    return sum

print(sum_non_question_elements(modified_matrix))