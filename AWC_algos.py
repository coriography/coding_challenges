
###** August 5, 2021 - intersection of two arrays II **###

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# intersectionOfArrays([1,2,2,1], [2,2]) => [2,2]
# intersectionOfArrays([4,9,5], [9,4,9,8,4]) => [4,9] OR [9,4]
# intersectionOfArrays([], [9,4,9,8,4]) => []

# Constraints:
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
 
# Follow up:
# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# for each num in nums1,
# if not already in dictionary,
# add to dictionary with value of 1
# else if in dictionary already:
# increment value of that key

# for each num in nums2,
# if in dictionary and value >0,
# add key to results list and decrement value by 1
# if not in dictionary, do nothing

# return results list

# def intersectionOfArrays(nums1, nums2):

#     nums1_dict = {}
#     intersection = []

#     for num in nums1:
#         nums1_dict[num] = nums1_dict.get(num, 0) + 1
    
#     for num2 in nums2:
#         if num2 in nums1_dict and nums1_dict[num2]:
#             intersection.append(num2)
#             nums1_dict[num2] -= 1
            
#     return intersection

# start a pointer at the beginning of both arrays, i and j
# sort both arrays in ascending order
# if nums1[i] and nums2[j] have the same value,
# add that value to the result list
# AND increment both pointers
# if nums1[i] and nums2[j] have different values, 
# increment the pointer at the lower value
# 
# OR -- if nums1[i] < nums2[j],
# increment i
# and if nums2[j] < nums1[i],
# increment j
# 
# stop when i equals the length of nums1
# # and j equals the lenght of nums2

###** July 23, 2021 - longest prefix **###

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# longestCommonPrefix(["flower","flow","flight"]) # => "fl"
# longestCommonPrefix([""]) # => ""
# longestCommonPrefix(["guppy"]) # => "guppy"

def longestCommonPrefix(list_of_words):
        
        # while j < len(first_word) ???????
            # for each string, starting at index 1,
                # if string at index j is the same as the first string's index j, 
                    # continue to next string
                # else, exit and return
            # increment j
            # increment prefix count
        # return
        
        # ["flower","flow","flight"]
        #            word
        #   j = 0
        
    j = 0
    first_word = list_of_words[0]
    prefix = ""
    
    if len(list_of_words) == 1:
        return first_word
    
    while j < len(first_word):
    
        for i in range(1, len(list_of_words)):

            word = list_of_words[i]
            
            if j < len(word):
            
                curr_letter = word[j]

                if curr_letter == first_word[j]:
                    pass
                else:
                    return prefix
            else:
                return prefix

        j += 1
        prefix += curr_letter
    
    return prefix

##** alternate solution with sorting
    # if not strs:
    #     return ""
    
    # strs.sort()
    
    # result = []
    
    # for idx, char in enumerate(strs[0]):
    #     if char == strs[-1][idx]:
    #         result.append(char)
    #     else:
    #         break
    
    # return "".join(result)

longestCommonPrefix(["flower","flow","flight"]) # => "fl"
longestCommonPrefix([""]) # => ""
longestCommonPrefix(["guppy"]) # => "guppy"


###** July 16, 2021 - Move Zeroes **###

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# def moveZeroes(nums):
#     i, j = 0, 0 # i deals with incrementing, j deals with zeroes
    
#     # for as many times as length of nums,
#         # if nums[i] is zero, 
#             # pop it off and add to end
#             # don't increment i
#         # else if nums[i] not zero,
#             # increment i
    
#     # if len(nums) <= 1:
#     #     return nums
        
#     while i < len(nums):
#         i += 1
#         if nums[j] == 0:
#             nums.append(nums.pop(j)) #!! popping from middle is inefficient
#         else:
#             j += 1
            
#     return nums
    

# def moveZeroes(nums):

#     ### another solution: SWAP
    
#         # traverse array and keep track of first zero in arr; swap it with current non-zero element
        
#         # [1,3,0,0,12]
#         #      1
#         #          i
        
#     index_of_first_zero = 0
        
#     for i in range(0, len(nums)):
#         if nums[i] != 0:
#             nums[i], nums[index_of_first_zero] = nums[index_of_first_zero], nums[i]
#             index_of_first_zero += 1

#     return nums

#* creative slicing solution from Rachael Gunter
# def moveZeroes(list):
#     count = 0
#     while 0 in list[count:]: 
#         if 0 in list:
#             list.append(0)
#             index = list.index(0)
#             list.pop(index)
#             count += 1
#     return list

#* JS solution from Travis Prol
# function algoPractice(arr, n)
# {
#     let count = 0; 
#     for (let i = 0; i < n; i++)
#         if (arr[i] != 0)
#             arr[count++] = arr[i]; 
#     while (count < n)
#         arr[count++] = 0;
# }

moveZeroes([0,1,0,3,12]) # => [1,3,12,0,0]
moveZeroes([0]) # => [0]
moveZeroes([0,0,1]) # => [1,0,0]


###** July 9, 2021 - Alternating Sort **###

# You are given an array of integers a. A new array b is generated by rearranging the elements of a in the following way:
# b[0] is equal to a[0]
# b[1] is equal to the last element of a
# b[2] is equal to a[1]
# b[3] is equal to the second-last element of a
# b[4] is equal to a[2]
# b[5] is equal to the third-last element of a
# etc.

# determine whether the new array b is sorted in strictly ascending order or not. 

# def alternatingSort(array):
#     b = []

#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         b.append(array[left])
#         left += 1

#         if left < right:
#             b.append(array[right])
#             right -= 1

#     print("result: ", b)
#     print("sorted: ", sorted(array))
#     return b == sorted(array)

# print(alternatingSort([1, 2, 3, 4, 5, 6, 7, 8])) # => False
# print(alternatingSort([1, 3, 5, 7, 8, 6, 4, 2])) # => True
# print(alternatingSort([1, 3, 5, 7, 6, 4, 2])) # => True

###** July 2, 2021 - restocking the warehouse **###

###** Restocking the Warehouse **###


# A purchasing manager must buy a specific number of units of an item to replenish the warehouse. The primary supplier has a list of containers, each with a number of units. The manager must purchase full containers in order, starting at container 0 and continuing until at least the desired number has been purchased. If there are not enough units available in the supplier's containers, they must be purchased from another supplier. If, on the other hand, any extra items are purchased, they must be resold. Determine the remaining number of items to be purchased or sold after purchasing from the primary supplier.

# Example
# itemCount = [10, 20, 30, 40, 15]
# target = 80

# The manager starts buying at index 0 and continues until all available units are purchased or until at least 80 units have been purchased. The manager will buy containers with itemCounts = 10 + 20 + 30 + 40 = 100. Since too many items were purchased, the number sold is purchased - target = 100 - 80 = 20 units.

# If the target = 130, the manager will purchase all of the units from the primary supplier for a total of purchases = 115.  Then another target - purchases = 130 - 115 = 15 additional units must be purchased.

# Function Description

# Complete the function restock in the editor below.

# restock has the following parameter(s):
#     int itemCount[n]:  an array of integers that denote the item counts of the each container in the order they must be purchased
#    int : target: an integer that denotes the target number of items needed
# Returns:
#     int:  number of units that must be resold or that must be purchased from an alternate supplier.

# Constraints

# 1 ??? number of items in itemCount ??? 105
# 1 ??? target ??? 109
# 1 ??? itemCount[i] ??? 109
#
# Complete the 'restock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY itemCount
#  2. INTEGER target
#

# def restock(item_count, target):
#     # iterate through itemCount and add 
#     # stop when current count is >= target OR end of itemCount
#     # compare current count to target and return difference
    
#     current_count = 0
    
#     for container_count in item_count:
#         if current_count < target:
#             current_count += container_count
#         else:
#             break
    
#     return abs(current_count - target)


# class Warehouse:
    
#     def __init__(self):
#         self.inventory = 0 # int - how many units we have
#         self.target = 0
#         self.excess = 0
#         self.deficit = 0
#         self.supply = None

#     def receive_todays_supply(self, supply:list, target:int):
#         if not supply:
#             raise ValueError("Cannot accept empty supply")
#         self.supply = supply
#         self.target = 0 if target < 0 else target
#         self.restock_supply()
#         print(f"{self.excess=}, {self.deficit=}")
    
#     def restock_supply(self):
#         for item in self.supply:
#             self.inventory += item
#             if self.inventory > self.target:
#                 break
#         self.set_excess_or_deficit()

#     def set_excess_or_deficit(self):
#         value = self.inventory - self.target
#         if value > 0:
#             self.excess = value
#         else:
#             self.deficit = abs(value)

        
# w = Warehouse()
# w.receive_todays_supply([10, 20, 30, 40, 15], 80)
# # print(w.__dict__)


# import unittest
# class TestWarehouse(unittest.TestCase):
#     def setUp(self):
#         self.w = Warehouse()
#         self.n = 0

#     def tearDown(self):
#         self.w = Warehouse()
#         self.n += 1
#         print(self.n)

#     def test_receive_todays_supply(self):
#         supply = [10, 20, 30, 40, 15]
#         target = 80
#         expected_excess = 20
#         expected_deficit = 0
#         self.w.receive_todays_supply(supply, target)
#         with self.subTest(msg="excess"):
#             self.assertEqual(expected_excess, self.w.excess, "incorrect")
#         with self.subTest(msg="deficit"):
#             self.assertEqual(expected_deficit, self.w.deficit, "incorrect")

#     def test_empty_supply(self):
#         supply = None
#         target = None
#         self.assertRaises(
#             ValueError,
#             self.w.receive_todays_supply,
#             supply, target
#             )
        


# if __name__ == '__main__':
#     unittest.main()


###** 6/25/21 - Bounded Ratio **###
# You are given an array of integers a and two integers l and r. You task is to calculate a boolean array b, where b[i] = true if there exists an integer x, such that a[i] = (i + 1) * x and l ??? x ??? r. Otherwise, b[i] should be set to false.

# Example

# For a = [8, 5, 6, 16, 5], l = 1, and r = 3, the output should be boundedRatio(a, l, r) = [false, false, true, false, true].
# For a[0] = 8, we need to find a value of x such that 1 * x = 8, but the only value that would work is x = 8 which doesn't satisfy the boundaries 1 ??? x ??? 3, so b[0] = false.
# For a[1] = 5, we need to find a value of x such that 2 * x = 5, but there is no integer value that would satisfy this equation, so b[1] = false.
# For a[2] = 6, we can choose x = 2 because 3 * 2 = 6 and 1 ??? 2 ??? 3, so b[2] = true.
# For a[3] = 16, there is no an integer 1 ??? x ??? 3, such that 4 * x = 16, so b[3] = false.
# For a[4] = 5, we can choose x = 1 because 5 * 1 = 5 and 1 ??? 1 ??? 3, so b[4] = true.

# def boundedRatio(array, l, r):
    
#     result = []
    
#     for i in range(len(array)):
#         # i+1 * x == array[i]
#         x = array[i] / (i+1)
#         result.append(l <= x <= r and x == int(x))

#     return result

# print(boundedRatio([8, 5, 6, 16, 5], 1, 3)) # => [false, false, true, false, true]


###** June 18, 2021 **###

# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Example 4:

# Input: s = ""
# Output: 0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ## !! doesn't work for SPACES
        # use a dict or str to track previously-counted letters
        # use a counter to track current count
        # use a list to track all counts once you hit a repeated letter
        
        # initialize all counts list
        # initialize "seen" container as empty
        # start count at 0
        
        # iterate through s with i
            # if letter is not in seen,
                # increase count
                # add letter to seen
            # if letter has been seen,
                # add count to all counts list
                # reset seen to empty and add this letter
                # set count to 1
        
        # return max of all counts
        
        all_consecutive_counts = [] # !! how can I optimize this? keep a running count?
        seen = "" #!! change this to a dict / abcabc "a"
        count = 0
        
        for letter in s:
            if letter not in seen:
                count += 1
                seen += letter
            else:
                all_consecutive_counts.append(count)
                seen = ""
                seen += letter
                count = 1
                
        if len(all_consecutive_counts) == 0:
            return 0
        else:
            return max(all_consecutive_counts)

    # !! refactor - returns wrong output
    # longest_so_far = 0
    #     # seen = "" # change this to a dict
    #     seen = {}
    #     count = 0
        
    #     for letter in s:
    #         if letter not in seen:
    #             count += 1
    #             seen[letter] = 1
    #             print(seen)
    #         else:
    #             if count > longest_so_far:
    #                 longest_so_far = count
    #             seen = {}
                # seen[letter] = 1
    #             count = 1
                
    #     return longest_so_far


###** June 04, 2021 - PREPROCESS DATES **####
# TODO: mention mentorship program!!!!!

# write a function called "preprocess_dates" that takes in dates in format 'day abbreviated_month year' ('30th Feb 1997')
# and returns dates in format 'year-number_month-two_digit_day' ('1997-02-30')
# input will always consist of valid dates in the expected format
# "day" may end in "st", "nd", "rd", "th"

# Input: an array of strings 
# Output: an array of re-formatted strings

# Examples:
# ['30th Feb 1997','1st Oct 2030','3rd Nov 1876','1st Dec 1865'] => ['1997-02-30','2030-10-01','1876-11-03','1865-12-01']

# def preprocessDate(dates):
#     # Write your code here
#     # split input on spaces => list of lists  [['00th', 'ABC', '0000'],['00th', 'ABC', '0000']]
#     # create a dictionary for months
#     # for each date in the dates list,
#         # edit date[0] by 
#             # slicing off last two char
#             # add a 0 if one digit
#         # edit month by changing to dict value
#         # don't edit year
    
#     months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
#     formatted_dates = [] # creating a new array of formatted data, assuming we want to keep the input data in its original state. if the priority is to save space, I would instead replace each date in the original dates array.
    
#     for i, date in enumerate(dates):
#         day, month, year = date.split()
#         day = day[0:-2]
#         if len(day) == 1:
#             day = f"0{day}"
#         month = months[month]
#         formatted_dates.append(f"{year}-{month}-{day}")
            
#     return formatted_dates


###*** May 28, 2021 - LETTERBOXES ***###

# ten friends started a side gig where they re-paint the numbers on mailboxes. Each person is assigned to one digit, 0 through 9. For example, somebody will paint only the 1's, somebody else will paint only the 2's and so on... At the end of the day, money is distributed based on the amount of work each person did. 

# given the start and end mailbox numbers, write a method to return the frequency of all 10 digits painted.
# output should be an array with a length of 10, corresponding to each digit painted.

# BONUS: add a third input of total dollars earned and compute an output of dollars each person is owed.

# EXAMPLE:
# paint_mailboxes(125, 132) => [1,9,6,3,0,1,1,1,1,1]

# 125 = 1, 2, 5
# 126 = 1, 2, 6
# 127 = 1, 2, 7
# 128 = 1, 2, 8
# 129 = 1, 2, 9
# 130 = 1, 3, 0
# 131 = 1, 3, 1
# 132 = 1, 3, 2

# 0 is painted 1 time
# 1 is painted 9 times
# 2 is painted 6 times
# etc.....

##### original
# def paint_mailboxes(start, finish):

#     d = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
#     all_char = []
    
#     for n in range(start, finish + 1):
        
#         for char in str(n):
#             all_char.append(char)
    
#     for c in sorted(all_char):
#         d[int(c)] += 1

#     return list(d.values())

####### refactored
# def paint_mailboxes(start, finish):
#     result = [0] * 10
# #     print(result)
#     for n in range(start, finish+1):
#         for i in str(n):
#             result[int(i)] += 1
#     return result

# ###### with bonus
# def paint_mailboxes_bonus(start, finish, dollars):
#     result = [0] * 10
    
#     for n in range(start, finish+1):
#         for i in str(n):
#             result[int(i)] += 1
    
#     total = sum(result)
#     # for each frequency, divide it by the total to get the percent
    
#     payout = []
#     for r in result:
#         percent_share = r/total
#         # multiply dollars received by percent and add formatted version to payout
#         payout.append(f'${dollars * percent_share:.2f}')
    
#     return print(payout)

# # paint_mailboxes(125, 132) # => [1,9,6,3,0,1,1,1,1,1]
# # paint_mailboxes(1000, 1015) # => [28, 24, 2, 2, 2, 2, 1, 1, 1, 1]
# # paint_mailboxes(1000, 2000) #=> [303, 1300, 301, 300, 300, 300, 300, 300, 300, 300]

# paint_mailboxes_bonus(125, 132, 1000) # => ['$41.67', '$375.00', '$250.00', '$125.00', '$0.00', '$41.67', '$41.67', '$41.67', '$41.67', '$41.67']
# paint_mailboxes_bonus(1000, 1015, 800) # => ['$350.00', '$300.00', '$25.00', '$25.00', '$25.00', '$25.00', '$12.50', '$12.50', '$12.50', '$12.50']
# paint_mailboxes_bonus(1000, 2000, 10000) #=> ['$756.74', '$3246.75', '$751.75', '$749.25', '$749.25', '$749.25', '$749.25', '$749.25', '$749.25', '$749.25']





###*** May 14, 2021 GETTRIPLES ***###

# Write a function called getTriples that takes a string and returns an array of index pairs of the start/end indices of any letter that occurs more than 3 times in a row
# get groups of 3 or more adjacent
# getTriples(''); // []
# getTriples('hello'); // []
# getTriples('helllooooo'); // [ [ 2, 4 ], [ 5, 9 ] ]
# getTriples('hhelllooooo'); // [ [ 3, 5 ], [ 6, 10 ] ]
# getTriples('hhhelllooooo'); // [ [ 0, 2 ], [ 4, 6 ], [ 7, 11 ] ]
# getTriples('hhhhhhhellloooooo'); // [ [ 0, 6 ], [ 8, 10 ], [ 11, 16 ] ]

# two pointers - i slow, j fast
# i only moves when j and j+i are not equal

# return less than 3 long
# i starts at word[0], j at word[1]
# for each char in word, 
# 

# def getTriples(word):
    
#     pairs = []
    
#     if len(word) < 3:
#         return print(pairs)
    
#     i, j = 0, 1
#     count = 0
    
#     while j < len(word) - 1:
        
#         while word[i] == word[j] and j < len(word) -1:
#             j += 1
#             count += 1
#         if word[i] != word[j] and count >= 3:
#             pairs.append([i, j-1])
#         i = j
#         j += 1
    
#     return print(pairs)

# getTriples(''); # // []
# getTriples('hello'); # // []
# getTriples('helllooooo'); # // [ [ 2, 4 ], [ 5, 9 ] ]
# getTriples('hhelllooooo'); # // [ [ 3, 5 ], [ 6, 10 ] ]
# getTriples('hhhelllooooo'); # // [ [ 0, 2 ], [ 4, 6 ], [ 7, 11 ] ]
# getTriples('hhhhhhhellloooooo'); #// [ [ 0, 6 ], [ 8, 10 ], [ 11, 16 ] ]


###*** May 07, 2021 ISSUBSEQUENCE ***###

# Write a function called isSubsequence which takes in two strings and checks whether the characters in the first string form a subsequence of the characters in the second string. In other words, the function should check whether the characters in the first string appear somewhere in the second string, without their order changing.
# isSubsequence("string", "imastring")
# isSubsequence("strung", "imastring")

# def isSubsequence(my_substr, my_str):
    
#     # start at end on both (while str AND substr?)
#         # pop off last letter of str
#         # if last letter of str matches substr, 
#             # store it
#             # pop off substr
#         # if it doesn't match, don't store it
#     # after reaching the end (beginning) of substr,
#     # return whether substr matches joined stored letters - REVERSED
    
#     matching = 0
    
#     def split(string):
#         return [char for char in string]
    
#     my_str = split(my_str)
#     new_substr = split(my_substr)
    
#     while new_substr and my_str:
#         curr = my_str.pop()
#         if  curr == new_substr[-1]:
#             matching += 1
#             new_substr.pop()
    
#     return print(matching == len(my_substr))
    
    
#     # return print(my_substr in my_str)
    
# isSubsequence('hello', 'hello world'); # true
# isSubsequence('sing', 'sting'); # true
# isSubsequence('abc', 'abraadabrac'); # true
# isSubsequence('abc', 'acb'); # false
# isSubsequence('abcd', 'abd')


###*** April 30, 2021 ISPALINDROME ***###
# def isPalindrome(str):
#     # find whether indices at same distance from beginning and end match
#     # can I use negative index in py?
    
#     # if str == '':
#     #     return False
#     # else:
#     #     count = 0
#     #     for i in range(0, len(str)): # change to while halfway for efficiency
#     #         if str[i] == str[-i -1]:
#     #             count += 1
#     # return print(count == len(str))

# #     d_str = {}
    
# #     if str == '':
# #         return False
# #     else:
# #         for i, char in enumerate(str):
# #             d_str[i] = char
            
# #         print(d_str)

#     # if str == '':
#     #     return False
#     # else:
#     #     count = 0
#     #     for i in range(0, len(str)): # change to while halfway for efficiency
#     #         if str[i] == str[-i -1]:
#     #             count += 1
#     # return print(count == len(str))
    
#     # 2 pointers
#     # start one at beg and one at end
#     # and 
            

# isPalindrome('') # false
# isPalindrome('racecar') # true
# isPalindrome('racecars') # false
# isPalindrome('race car') # false

###*** April 29, 2021 (with Brian) PHOENETIC ARRAY ***###
# Question:Convert an array of integers into an array of stringsrepresenting the phonetic equivalent of theinteger.For example:Given an array: [3, 25, 209], print???Three,TwoFive,TwoZeroNine???into stdout.Given an array: [10, 300, 5], print???OneZero,ThreeZeroZero,Five???into stdout.

# output: arr[strs]
# phoen = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}

# def splitStr(str):
#     return [char for char in str]

# # result = []

# # print(splitStr("cori"))

# def intToStr(listInt):
#     result = []
    
#     for curr in listInt:
#         curr = str(curr)
#         split = splitStr(curr)
#         # print(split)
#         for i, char in enumerate(split):
#         # swap int for val
#             split[i] = phoen[int(char)]
#         # print(split)
#         # concatenate
#         result.append("".join(split))
#         # push curr to result arr
#     print(result)
    
# intToStr([3, 25, 209])
# intToStr([10, 300, 5])


###*** April 23, 2021 - MAX SUBARRAY SUM***###
#  Write a function called maxSubarraySum which accepts an array of integers and a number called n. the function should calculate the maximum sum of n consecutive elements in the array.

# maxSubarraySum([1, 2, 3, 4, 5, -1, -2], 3); // 12
# maxSubarraySum([2, 6, 9, 2, 1, 8, 5, 6, 3], 4); //22
# maxSubarraySum([1, 2], 3)
# maxSubarraySum([], 4); // null

# def maxSubarraySum(arr, n):
#     """returns maximum sum of n consecutive elements in an array"""
    
#     ### slice + add each num in slice
    
#     # create new arr
    
#     # while arr[n] exists:
#         # iterate through elements by index
#             # slice 0 to n
#             # add elements and append to new arr
#             # increment index
    
#     # return max of new arr
#     curr_result = 0
#     new_arr = []
    
#     if len(arr) < n:
#         return sum(arr)
    
#     for i in range(0, len(arr)):
#         new_arr.append(sum(arr[i:i+n]))
        
#     return max(new_arr)
    
#     ### two pointers - start n apart and advance until end of arr
#     ### evaluate last n elements, pop off last 1 el, repeat - + recursive solve
    
#     # take care of edge case: empty arr - return None
#     # ^+ length of arr is smaller than n
#         # loop through all elements and add together
    
#     # instantiate max var as None OR as array
#     # while length of arr is >= n,
#         # loop through last n elements
#             # add each together
#             # store sum - if greater than max var, sub it. OR append to array
#             # pop off last element
#     # return max var OR max(new array)
    
# #     if not arr:
# #         return None
    
# #     max_results = []
# #     curr_result = 0
    
# #     if len(arr) < n:
# #         for el in arr: 
# #             curr_result += el
# #         return curr_result
# #     else:
# #         while len(arr) >= n:
# #             curr_result = 0
# #             n_el = arr[-n:]
# #             for el in n_el: 
# #                 curr_result += el
# #             # print curr_result
# #             max_results.append(curr_result)
# #             arr.pop()
# #             # print(arr)
    
# #     return max(max_results)
    

# print(maxSubarraySum([1, 2, 3, 4, 5, -1, -2], 3))
# print(maxSubarraySum([2, 6, 9, 2, 1, 8, 5, 6, 3], 4))
# print(maxSubarraySum([1, 2], 3))
# print(maxSubarraySum([], 4))

###*** April 16, 2021 ***###
#  write a function called sumZero that accepts a sorted array of integers and returns the index pair of the integers that add up to zero
#  if no index pair adds up to 0, return []
# sumZero([-3, -3, -1, 0, 1, 2, 5]); // [2, 4]
# sumZero([-3, -2, -1, 0, 1, 2, 3]); // [0, 6]
# sumZero([1, 2, 3]); // []

# use two pointers

# def sumZero(slist):
# """two pointers solution"""
    
#     # i = 0
#     for i in range(0, len(slist)-1):
#         for j in range(1, len(slist)):
#             if slist[i] + slist[j] == 0:
#                 # print("equal zero")
#                 return print([i, j])
            
#     return print([])

# def sumZero(slist):
#     """dictionary solution"""

#     # iterate through list
#     # if opposite of current num not in dictionary,
#     # add current num with its index as value
#     # else,
#     # return opposite's index and current index
#     # else else return empty list

#     seen = {} 
#     pairs = []

#     for i, curr in enumerate(slist):
#         if -curr not in seen:
#             seen[curr] = i
#         else:
#             pairs.append([seen[-curr], i])

#     return print(pairs)


    
# # assert(sumZero([-3, -3, -1, 0, 1, 2, 5]) == [2,4], "wrong")
# # assert(sumZero([-3, -2, -1, 0, 1, 2, 3]) == [0, 6], "wrong")
# # assert(sumZero([1, 2, 3]) == [], "wrong")
# sumZero([-3, -3, -1, 0, 1, 2, 5])
# sumZero([-3, -2, -1, 0, 1, 2, 3])
# sumZero([1, 2, 3])


# notes: define a left pointer and a right pointer
# if sum > 0, decrement right; if sum < 0, increment left



# JS solution:
# const sumZero = (arr) => {
#   let start = 0;
#   let end = 0;
#   for (
#     let i = 0, j = arr.length - 1;
#     i <= Math.ceil(arr.length / 2);
#     i += start, j -= end
#   ) {
#     console.log('start:', start, 'end:', end)
#     if (arr[i] + arr[j] === 0) return [j, i];
#     if (arr[i] + arr[j] > 0) {
#       end=1
#       start=0
#     }
#     if (arr[i] + arr[j] < 0) {
#       start=1
#       end=0
#     }
#   }
#   return [];
# };
# console.log(sumZero([-3, -3, -1, 0, 1, 2, 5, 7, 9, 11, 13, 112, 1154])); // [2, 4]