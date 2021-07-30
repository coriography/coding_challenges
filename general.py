
###** contains duplicate **###
# https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums: List[int]) -> bool:
        # iterate through vals
        # if in dict, return true
        # else add to dict and continue
        # return false
        
        # d_nums = {}
        
        # for num in nums:
        #     if num in d_nums:
        #         return True
        #     else:
        #         d_nums[num] = 1
                
        # return False

###** move zeroes **###

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/567/

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i, j = 0, 0
        
#         # [0,1]
#         #  i 
#         # [0]
        
#         # i deals with incrementing
#         # j deals with zeroes
        
#         # for as many times as length of nums,
#             # if nums[i] is zero, 
#                 # pop it off and add to new array # [0]
#                 # don't increment i
#             # else if nums[i] not zero,
#                 # increment i
                
#         # extend nums with new array
        
#         # if len(nums) <= 1:
#         #     return nums
            
#         while i < len(nums):
#             i += 1
#             if nums[j] == 0:
#                 nums.append(nums.pop(j))
#             else:
#                 j += 1
                
#         return nums

###** Buy and sell stocks II **###
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/


# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
        
#         # buy helper function
#         # sell helper function
        
#         # evaluate difference between current and next
#         # add differences
        
#         profit = 0
        
#         if len(prices) <= 1:
#             return 0
        
#         for i in range(1, len(prices)):
#             if prices[i] > prices[i-1]:
#                 profit += prices[i] - prices[i-1]
            
            
#         return profit

###** number of steps to zero **###
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# class Solution:
#     def numberOfSteps(self, num: int) -> int:
        
#         num_steps = 0
        
#         while num > 0:
#             num_steps += 1
#             if num % 2 == 0:
#                 num = num/2
#             else:
#                 num = num - 1
                
#         return num_steps

###### ** ABBREVIATE WORDS ** ######

def abbreviate(s):
    # print(s)

    def gen_words(s):
        word = []
        for c in s:
            if c.isalpha():
                word.append(c)
            else:
                if word:
                    yield "".join(word)
                yield c
                word = []
        if word:
            yield "".join(word)

    def abbreviate_word(word):
        if len(word) < 4:
            return word
        abbreviation = {"first_char": word[0], "length": len(word[1:-1]),
                        "last_char": word[-1]}
        return "{first_char}{length}{last_char}".format(**abbreviation)

    # print([word for word in gen_words(s)])
    return print("".join(abbreviate_word(word) for word in gen_words(s)))
    
abbreviate("elephant-rides are really fun!") # => "e6t-r3s are r4y fun!"


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