'''
1 Oski Stole Your Power
Oski hacked your computer and you can no longer use x**y or pow(x, y). Find
a different way (by writing a function) that can compute x raised to the power
of y.
>>> x = 2
>>> y = 3
>>> computePower(x, y)
8
'''
def computePower(x,y):
    #I know that x to the power of y is x multiplied by itself y times
    #Thus, I will multiply x by itself
    product_of_X = 1

    while y > 0:
        product_of_X *= x
        y-=1
    
    return product_of_X

solution = computePower(2,3)
print(solution)
'''
2 What Should I Wear?
You are trying to decide what to wear to the Python DeCal lecture, but you
are only concerned about the day’s lowest and highest temperatures. Write a
function that takes in a list as input and returns a tuple with two values.
>>> readings = [15, 14, 17, 20, 23, 28, 20]
>>> temperatureRange(readings)
(15.6, 22.1)
'''
def temeratureRange(x,y,a,b,c,d,e):
    list = [x,y,a,b,c,d,e]
    extremas = (max(list), min(list))
    return extremas

temperatures = temeratureRange(15, 14, 17, 20, 23, 28, 20)
print(temperatures)
'''
3 Check if its the Weekend
All your classes have assigned problem sets due next week, and you want to
check if it’s the weekend so you have time to work on them. Write a function
that takes a day of the week (represented as an integer, where 1 = Monday, 2
= Tuesday, etc) and returns True if its a weekend and False if otherwise.
>>> day = 6 # Saturday
>>> isWeekend(day)
True
1
'''
def isWeekend(day):
    if (day > 5):
        return True
    else:
        return False
    
day = 6
checkday = isWeekend(day)
print(checkday)
'''
4 Fuel Efficiency Calculator
The Python DeCal wants to take a trip to the Lick Observatory ( San Jose,
CA) and they want to pick the best car. Write a function that takes the distance
traveled (in miles) and the amount of fuel consumed (in gallons) as input and
returns the fuel efficiency.
>>> distance = 70 # miles
>>> fuel = 21.5 # gallons
>>> fuel_efficiency(distance, fuel)
3.26
'''
def fuel_efficiency(distance, fuel):
    result = distance / fuel
    return round(result , 2)

distance = 70
fuel = 21.5

efficiency = fuel_efficiency(distance, fuel)
print(efficiency)
'''
5 Secret Code
Write a function that takes an integer as input and moves its last digit to the
front of the number. You may NOT convert the input to a string. Hint: Try
modulus (%) and floor division. (\\) to solve this problem.
>>> n = 12345
>>> decodeNumbers(n)
51234
'''
def decodeNumbers(n):
    last_digit = n % 10
    cut_number = n // 10
    multiplier = 1
    n_length = 11

    while n_length >= 10:
        n_length = n / multiplier
        multiplier = multiplier * 10

    final_number = ((multiplier / 10) * last_digit) + cut_number
    int_final_number = int(final_number)
    return int_final_number

n = 12345
last_digit_to_front = decodeNumbers(n) 
print(last_digit_to_front)
'''
6 Min & Max but with Loops!
Oh no! Oski hacked you computer again... now you have lost the ability to use
min() and max().

6.1 For Loops
Write two functions to manually find the minimum and maximum values in a
list of numbers with for loops.
>>> nums = [2024, 98, 131, 2, 3, 72]
>>> find_min_with_for_loop(nums)
2
>>> find_max_with_for_loops(nums)
2024
'''
def find_max_with_for_loop(nums):
    biggest_num = nums[0]
    for num in (nums):
        if num > biggest_num:
            biggest_num = num
    return biggest_num

def find_min_with_for_loop(nums):
    smallest_num = nums[0]
    for num in (nums):
        if num < smallest_num:
            smallest_num = num
    return smallest_num

nums = [2024, 98, 131, 2, 3, 72]

max_number_with_for_loop = find_max_with_for_loop(nums)
min_number_with_for_loop = find_min_with_for_loop(nums)

print (max_number_with_for_loop)
print (min_number_with_for_loop)
'''
6.2 While Loops
Write two functions to manually find the minimum and maximum values in a
list of numbers with while loops.
>>> nums = [2024, 98, 131, 2, 3, 72]
>>> find_min_with_while_loop(nums)
2
>>> find_max_with_while_loops(nums)
2024
'''
def find_max_with_while_loop(nums):
    biggest_num = nums[0]
    x = 0
    while(x < len(nums)):
        if nums[x] > biggest_num:
            biggest_num = nums[x]
        x = x + 1
    return biggest_num   
 
def find_min_with_while_loop(nums):
    smallest_num = nums[0]
    x = 0
    while(x < len(nums)):
        if nums[x] < smallest_num:
            smallest_num = nums[x]
        x = x + 1
    return smallest_num  
    
nums = [2024, 98, 131, 2, 3, 72]

max_number_with_while_loop = find_max_with_while_loop(nums)
min_number_with_while_loop = find_min_with_while_loop(nums)

print(max_number_with_while_loop)
print(min_number_with_while_loop)
'''
7 Counting Vowels
Write a function that takes a string as an input and returns the number of vowels
in the string and the number of consonants in the string as tuple. Don’t forget
about capital letters! Hint: You can use .isalpha() to check if a character is
a letter.
>>> text = "UC Berkeley, founded in 1868!"
>>> vowel_and_consonant_count(text)
(4, 11)
'''
def vowel_and_consonant_count(text):
    vowel_count = 0
    consonant_count = 0
    vowel = "aeiouAEIOU"
    consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    for char in text:
        if char.isalpha():
            if char in vowel:
                vowel_count = vowel_count + 1
            if char in consonant:
                consonant_count = consonant_count + 1
    vowel_consonant = (vowel_count, consonant_count)
    return vowel_consonant

text = "UC Berkeley, founded in 1868!"
vowel_constant = vowel_and_consonant_count(text)
print(vowel_constant)
'''
8 Calculate Digital Root
Write a function that takes an integer as an input and returns the sum of its
digits.
>>> num = 2468
>>> digital_root(num)
20
'''
def digital_root(num):
    digit_list = []

    while num > 0:
        digit_list.append(num % 10)
        num = num // 10
    digit_sum = sum(digit_list)
    return digit_sum

num = 2468
number_sum = digital_root(num)
print(number_sum)