
###** June 04, 2021 - PREPROCESS DATES **####
# write a function called "preprocess_dates" that takes in dates in format 'day abbreviated_month year' ('30th Feb 1997')
# and returns dates in format 'year-number_month-two_digit_day' ('1997-02-30')
# input will always consist of valid dates in the expected format
# "day" may end in "st", "nd", "rd", "th"

# Input: an array of strings 
# Output: an array of re-formatted strings

# Examples:
# ['30th Feb 1997','1st Oct 2030','3rd Nov 1876','1st Dec 1865'] => ['1997-02-30','2030-10-01','1876-11-03','1865-12-01']

def preprocessDate(dates):
    # Write your code here
    # split input on spaces => list of lists  [['00th', 'ABC', '0000'],['00th', 'ABC', '0000']]
    # create a dictionary for months
    # for each date in the dates list,
        # edit date[0] by 
            # slicing off last two char
            # add a 0 if one digit
        # edit month by changing to dict value
        # don't edit year
    
    months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    formatted_dates = [] # creating a new array of formatted data, assuming we want to keep the input data in its original state. if the priority is to save space, I would instead replace each date in the original dates array.
    
    for i, date in enumerate(dates):
        day, month, year = date.split()
        day = day[0:-2]
        if len(day) == 1:
            day = f"0{day}"
        month = months[month]
        formatted_dates.append(f"{year}-{month}-{day}")
            
    return formatted_dates


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
# Question:Convert an array of integers into an array of stringsrepresenting the phonetic equivalent of theinteger.For example:Given an array: [3, 25, 209], print“Three,TwoFive,TwoZeroNine”into stdout.Given an array: [10, 300, 5], print“OneZero,ThreeZeroZero,Five”into stdout.

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
    
#     # i = 0
#     for i in range(0, len(slist)-1):
#         for j in range(1, len(slist)):
#             if slist[i] + slist[j] == 0:
#                 # print("equal zero")
#                 return print([i, j])
            
#     return print([])

    
# # assert(sumZero([-3, -3, -1, 0, 1, 2, 5]) == [2,4])
# # assert(sumZero([-3, -2, -1, 0, 1, 2, 3]) == [0, 6])
# # assert(sumZero([1, 2, 3]) == [])
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