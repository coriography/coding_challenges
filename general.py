
###### ** ABBREVIATE WORDS ** ######

# def abbreviate(s):
#     import re
    
#     # "elephant-rides are really fun!"
#     #  i      j\

#     # split string on spaces
#     words_of_s = s.split()
#     print(words_of_s)
#     # iterate through words
#     for word in words_of_s:
#         print(word)
#         # if word is greater than 3 char,
#         if len(word) > 3:
#             ### TWO POINTERS
#                 # start i at 0
#             i = 0
#                 # for j in range(1, len(word) - 1)
#             for j in range(1, len(word) -1):
#                 # print("word[j]: ", word[j])
#                     # if word[j+1] is not alpha, 
#                 if not word[j+1].isalpha():
#                     print('not alpha!')
#                     word = re.split('\W+', word)
                
#                 # for w in word:
#                 #     print(w)
#                     # first, middle, last = w[i], w[i+1:j-1], w[j]
#                     # middle = len(middle)
#                     # new_word = f"{first}{middle}{last}"
#                     # print(new_word)
#                         # delete everything between i and j and replace with number
#                     # else:
#                         # continue
            
#             ### OR SLICING ##! doesn't account for non-alpha
#                 # slice first, last, and everything else
#                 # first, middle, last = word[0:1], word[1:-1], word[:-1]
#                 # print(word)
#                 # print(middle)
#                 # replace with length of that slice
#                 # paste first, length, last together
            
#     # return joined split string

# abbreviate("elephant-rides are really fun!") # => "e6t-r3s are r4y fun!"

###### ** MULTIPLICATION TABLE ** ######

# def multiplication_table(n):
#     # https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python

#     table = []
    
#     for i in range (1, n+1):
#         curr_row = []

#         for j in range(1, n+1):
#             # append product of j and i
#             curr_row.append(j*i)
#         table.append(curr_row)
    
#     return table



###### ** REPLACE WITH ALPHABET POSITION ** ######

# Given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

# def alphabet_position(text):
    
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     text_in_ints = []
    
#     for char in text:
#         char = char.lower()
        
#         if char in alpha:
#             text_in_ints.append(str(alpha.index(char) +1))
                                
#     return " ".join(text_in_ints)


####** TAX BRACKETS **####

# TODO: The tax bracket breaks at $86,375 - incomes >= $86,376 are taxed 24%, and incomes <= $86,375 are taxed 22%.
#?? what is the lowest salary in the 24% tax bracket where the take-home pay is higher than the top of the 22% tax bracket?
#?? return the total salary, the total amount of tax per year on that salary, and the take-home pay.

# def find_lowest_in_bracket(lo_tax_rate, max_lo_salary, hi_tax_rate, min_hi_salary):
#     """Finds the lowest salary in given tax bracket where the take-home pay is higher than the top of the lower tax bracket"""

#     # find max take-home pay of lower bracket
#     max_take_home_lower_bracket = max_lo_salary - (lo_tax_rate/100) * max_lo_salary
    
#     # iterative solution: loop through int starting at min_hi_salary until take-home pay is higher than max_take_home_lower_bracket
#     # "binary search"/logn solution: requires additional input of max_hi_salary

#     optimal_min_salary = min_hi_salary
#     optimal_min_take_home_pay = 0
#     optimal_min_tax = 0

#     while optimal_min_take_home_pay < max_take_home_lower_bracket:
        
#         optimal_min_tax = (hi_tax_rate/100) * optimal_min_salary
#         optimal_min_take_home_pay = optimal_min_salary - optimal_min_tax

#         optimal_min_salary += 1
    
#     return print(f"total minimum salary with highest take-home pay: {optimal_min_salary}\ntotal tax: {optimal_min_tax}\ntotal take-home pay: {optimal_min_take_home_pay}")

# find_lowest_in_bracket(22, 86375, 24, 86376)