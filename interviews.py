
###** Author History from API **###

# Complete the 'getAuthorHistory' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING author as parameter.
#
# Base urls:
#   https://jsonmock.hackerrank.com/api/article_users?username=
#   https://jsonmock.hackerrank.com/api/articles?author=
#

import requests

def getAuthorHistory(author):
    # initialize history as array to store list of strings
    # query API to retrieve author data
    # store about field IF it has a value
    # query API to retrieve list of author's articles
    # add title from each record to history array
        # if title is empty or none, use story_title
        # if both are empty or none, ignore record
    # fetch all data based on total_pages count and repeat last two steps
    # return history

    history = []
    
    base_users_url = "https://jsonmock.hackerrank.com/api/article_users?username="
    my_users_url = base_users_url + author
    
    r = requests.get(my_users_url)
    json_response = r.json()
    users_data = json_response["data"][0]
    
    about_author = users_data.get("about", None)
    
    if about_author != None and about_author != "":
        history.append(about_author)
        
    
    base_articles_url = "https://jsonmock.hackerrank.com/api/articles?author="
    my_articles_url = base_articles_url + author
    
    r_articles = requests.get(my_articles_url)
    json_response_articles = r_articles.json()

    total_pages = json_response_articles["total_pages"]

    for i in range(1, total_pages + 1):
        ## update URL to page i
        my_articles_url += "&page={i}"
        r_articles = requests.get(my_articles_url)
        json_response_articles = r_articles.json()

        data_articles = json_response_articles["data"]
        
        for article in data_articles:
            get_title = article.get("title", "story_title")
            if get_title != None and get_title != "":
                history.append(get_title)
    
        
    return history

print(getAuthorHistory("epaga"))
print(getAuthorHistory("saintamh"))
print(getAuthorHistory("olalonde"))



###** Restocking the Warehouse **###


# A purchasing manager must buy a specific number of units of an item to replenish the warehouse. The primary supplier has a list of containers, each with a number of units. The manager must buy contiguous containers, starting at container 0 and continuing until at least the desired number has been purchased. If there are not enough units available, they must be purchased from another supplier. If any excess items must be purchased, they must be resold. Determine the remaining number of items to be purchased or sold after purchasing from the primary supplier.

# Example
# n=5
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

# 1 ??? n ??? 105
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

def restock(item_count, target):
    # iterate through itemCount and add 
    # stop when current count is >= target OR end of itemCount
    # compare current count to target and return difference
    
    current_count = 0
    
    for container_count in item_count:
        if current_count < target:
            current_count += container_count
        else:
            break
    
    return abs(current_count - target)



###** Points Covering Segments **###

# You are given an array of segments (pairs that represent the lower and upper bounds of a segment, inclusive). Determine the minimum number of points that can be placed somewhere on the number line, so that each segment contains at least one point.

def segmentsCovering(array):
    pass

print(segmentsCovering([[-1, 3], [-5, -3], [3, 5], [2, 4], [-3, -2], [-1, 4], [5, 5]])) # => 3 (you can place 3 points at -3, 3, and 5 to cover all segments)
[[-5, -3], [-3, -2], [-1, 3], [-1, 4], [2, 4], [3, 5], [5, 5]]
# compare 1b with 2a
# if 1b >= 2a
    # compare min(1b, 2b) with 3a
    # if min >= 3a, move to 4a
    # if not, restart algo with 3a

# increase count whenever restarting with new segment
# check out leetcode merge intervals


###** Alternating Sort **###

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
#     result = []

#     left = 0
#     right = len(array) - 1 # 3

#     while left <= right:
#         result.append(array[left]) # b = [0, 3, 1]
#         left += 1 # 2

#         if left < right:
#             result.append(array[right]) # b = [0, 3, 1, 2]
#             right -= 1 # 2

#     print("result: ", result)
#     print("sorted: ", sorted(array))
#     return result == sorted(array)

# print(alternatingSort([1, 2, 3, 4, 5, 6, 7, 8])) # => False
# print(alternatingSort([1, 3, 5, 7, 8, 6, 4, 2])) # => True
# print(alternatingSort([1, 3, 5, 7, 6, 4, 2])) # => True


###** Order By ASC/DESC **###

# As a part of this problem, we're going to build, piece-by-piece,
# the part of a relational database that can take a list of rows and
# sort them by multiple fields:

# i.e., the part that implements
#       ORDER BY name ASC, age DESC

# Step 1: we want to write a function that returns the record
#         with the smallest entry of a given key
#
#         Treat missing keys as 0

# def min_by_key(arr, key):
#     # Your code here
#     pass

# records = [
#     {'a': 1, 'b': 4},
#     {'a': 3, 'b': 1},
#     {'a': 2}, 
#     {'a': -2, 'b': 2},
#     {'b': 3}
# ]

# print('min_by_key')
# print(min_by_key(records, 'a')) # -> {a: -2, b: 2}
# print(min_by_key(records, 'b')) # -> {a: 2}, since we treat b as 0


###** Mean Groups **###


# You are given an array of arrays a. Your task is to group the arrays a[i] by their mean values, so that arrays with equal mean values are in the same group, and arrays with different mean values are in different groups.

# Each group should contain a set of indices (i, j, etc), such that the corresponding arrays (a[i], a[j], etc) all have the same mean. Return the set of groups as an array of arrays, where the indices within each group are sorted in ascending order, and the groups are sorted in ascending order of their minimum element.

# Example

# For

# a = [[3, 3, 4, 2],
#      [4, 4],
#      [4, 0, 3, 3],
#      [2, 3],
#      [3, 3, 3]]
# the output should be

# meanGroups(a) = [[0, 4],
#                  [1],
#                  [2, 3]]
# mean(a[0]) = (3 + 3 + 4 + 2) / 4 = 3;
# mean(a[1]) = (4 + 4) / 2 = 4;
# mean(a[2]) = (4 + 0 + 3 + 3) / 4 = 2.5;
# mean(a[3]) = (2 + 3) / 2 = 2.5;
# mean(a[4]) = (3 + 3 + 3) / 3 = 3.
# There are three groups of means: those with mean 2.5, 3, and 4. And they form the following groups:

# Arrays with indices 0 and 4 form a group with mean 3;
# Array with index 1 forms a group with mean 4;
# Arrays with indices 2 and 3 form a group with mean 2.5.
# Note that neither

# meanGroups(a) = [[0, 4],
#                  [2, 3],
#                  [1]]
# nor

# meanGroups(a) = [[0, 4],
#                  [1],
#                  [3, 2]]
# will be considered as a correct answer:

# In the first case, the minimal element in the array at index 2 is 1, and it is less then the minimal element in the array at index 1, which is 2.
# In the second case, the array at index 2 is not sorted in ascending order.
# For

# a = [[-5, 2, 3],
#      [0, 0],
#      [0],
#      [-100, 100]]
# the output should be

# meanGroups(a) = [[0, 1, 2, 3]]
# The mean values of all of the arrays are 0, so all of them are in the same group.

# def meanGroups(a):
    
#     dict_of_avgs = {}

#     # find mean of each array
#     for i, lst in enumerate(a):
#         avg = sum(lst) / len(lst)
#         # add to dict with mean as key, array's index as value (in list)
#         if avg not in dict_of_avgs:
#             dict_of_avgs[avg] = [i]
#         else: 
#             dict_of_avgs[avg].append(i)

#     # output dict values as list
#     index_vals = list(dict_of_avgs.values())
#     # sort mega list
    
#     return index_vals
    


###** Bounded Ratio **###
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


###** Dedupe array **###

# write a function dedupe array that takes in an array of strings
# edge cases: empty array, one item in array

# def dedupe_array(list_of_str):
#     # convert list to set, convert back to an list
#     set_of_str = set(list_of_str)
    
    
#     # iterate through list
#     # for each item, if not in dict, add to dict
#     # if already in dict, don't do anything
#     # use dict.values() and convert to list
#     # OR just set strings as keys (unique)
    
#     return list(set_of_str)

# print(dedupe_array(['hi', 'hello', 'hi'])) # => ['hi', 'hello']
# print(dedupe_array(['meow', 'scratch', 'climb'])) # => ['meow', 'scratch', 'climb']


###** ID card validation **###

# Say, an organization issues ID cards to its employees with unique ID codes. The ID code for an employee named Jigarius Caesar looks as follows: CAJI202002196.

# Here???s how the ID code is derived:

# CA: First 2 characters of the employee???s last name.
# JI: First 2 characters of the employee???s first name.
# 2020: Full year of joining.
# 02: 2 digit representation of the month of joining.
# 19: Indicates that this is the 19th employee who joined in Feb 2020.
# This will have at least 2 digits, starting with 01, 02, and so on.

# (I didnt do this part with the verification digit)
# 6: The last digit is a verification digit which is computed as follows:
# Take the numeric part of the ID code (without the verification digit).
# Sum all digits in odd positions. Say this is o.
# Sum all digits in even positions. Say this is E.
# Difference between O & E. Say this is V.
# If V is negative, ignore the sign, e.g., -6 is treated as 6. Say this is V.
# If V is greater than 9, divide it by 10 and take the reminder. Say this is V.
# V is the verification code.

# Write a command-line program in your preferred coding language that:
# Allows the user to enter their First name, Last name and ID code.
# Prints PASS if the ID code seems valid.
# Prints INVESTIGATE otherwise.
# Write relevant tests.
# It is not necessary to use a testing library.
# You can use your custom implementation of tests.
# list of valid years
# list of valid months (01, 02, 03...12)

# define function that takes in first, last, and id as parameters
# check if first 2 characters of id match first 2 characters of first
# check if 3rd and 4th characters of id match first 2 characters of last
# create list of valid years we can check against
# check if 5th - 8th characters are in valid year list
# check if 9th-10th characters are in valid month list

# def get_user_input():
#     first = input("What is your first name: ")
#     last = input("What is your last name: ")
#     id_code = input("What is your id code?: ")

#     return [first, last, id_code]

# def check_last(last, id_code):
#     if last[0] == id_code[0] and last[1] == id_code[1]:
#         return True
#     return False

# def check_first(first, id_code):   
#     if first[0] == id_code[2] and first[1] == id_code[3]:
#         return True
#     return False

# def check_year(id_code):
#     valid_years = ["2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
#     if id_code[4:8] in valid_years:
#         return True
#     return False

# def check_month(id_code):
#     valid_months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
#     if id_code[8:10] in valid_months:
#         return True
#     return False

# def run_program():
#     first, last, id_code = get_user_input()
#     is_last_valid = check_last(last, id_code)
#     if not is_last_valid:
#         return "INVESTIGATE LAST NAME"
#     is_first_valid = check_first(first, id_code)
#     if not is_first_valid:
#         return "INVESTIGATE FIRST NAME"
    
#     is_month_valid = check_month(id_code)
#     if not is_month_valid:
#         return "INVESTIGATE MONTH"

#     is_year_valid = check_year(id_code)
#     if not is_year_valid:
#         return "INVESTIGATE YEAR"

#     return "PASS"

# print(check_month("pean202105"))

# def test_run_program(first, last, id_code):
#     # first, last, id_code = get_user_input()
#     is_last_valid = check_last(last, id_code)
#     if not is_last_valid:
#         return "INVESTIGATE LAST"
#     is_first_valid = check_first(first, id_code)
#     if not is_first_valid:
#         return "INVESTIGATE FIRST"
    
#     is_month_valid = check_month(id_code)
#     if not is_month_valid:
#         return "INVESTIGATE MONTH"

#     is_year_valid = check_year(id_code)
#     if not is_year_valid:
#         return "INVESTIGATE YEAR"

#     return "PASS"
# #expecting pass
# print(test_run_program("anna", "peery", "pean202105"))
# #expecting fail
# print(test_run_program("anna", "peery", "zzee202105"))
# #expecting fail
# print(test_run_program("jen", "brissman", "brjb555599"))




###** NON-CONSTRUCTIBLE CHANGE **###

# given an array of positive int representing the value of non-unique coins in your pocket, write a function that returns the minimum amount of change you cannot create.


def find_min_change(pocket_change):
    """finds minimum change possible from given pocket change.
    >>> (find_min_change([1,2,5]))
    4
    >>> (find_min_change([5,7,1,1,2,3,22]))
    20
    """
    # [5,7,1,1,2,3,22]
    #  i
    #    j
    # current_min_change = 1

    # start curr_min_change at 1
    # sort pocket change
    # iterate through each coin (while pocket_change)
    # if curr_coin equals curr_min_change, 
        # increase curr_min_change
        # increment curr_coin
    # if curr_coin <= curr_min_change,
        # sum curr_coin with curr_min_change and all the int below curr_min_change down to 1
        # if none of these sums equal curr_coin,
            # return curr_min_change
        # else
            # increment curr_coin

    return pocket_change

# print(find_min_change([5,7,1,1,2,3,22])) # 20
# print(find_min_change([1,2,5])) # 4

###** PREPROCESS DATES **####
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
    

###** ARE THEY SPEEDING? **####
# def is_speeding(list_data):
    
#     # input at zero = first point
#     # input 1 = second point
    
#     # third item from second el of list minus
#     # take third item from first element of list
    
#     # divide all by
#     # first item of second list minus
#     # first item of first list
    
#     # return whether the result of above is over 100 - true/false
#     # + license plate
    
# #     while list_data:
    
# #         i_1, i_2 = list_data[0], list_data[1]

# #         time_1, time_2 = i_1[2], i_2[2]
# #         position_1, position_2 = i_1[0], i_2[0]

# #         speed = (position_2 - position_1) / ((time_2 - time_1)/3600)

# #         print([f'{i_1[1]}', speed > 100])
        
# #         list_data.pop(0)
# #         list_data.pop(0)

# # create dict
# # iterate through input
# # check whether license plate in dict
# # if not, add license plate as key
# # add value position, time
# # if already in dict
# # calculate speed & print boolean & license

#     license_lookup = {}

#     for speed_data in list_data:
#         position, license, timestamp = speed_data
#         if license not in license_lookup:
#             license_lookup[license] = [position, timestamp]
#         else:
#             # speed = (position_2 - position_1) / ((time_2 - time_1)/3600)
#             speed = (position - license_lookup[license][0]) / ((timestamp - license_lookup[license][1])/3600)
#             print(license, speed > 100)
#             # TODO: refactor for out-of-order        

# # print(is_speeding([[1, "ABC-123", 1599066000], [2, "ABC-123", 1599066030], [1, "DEF-123",1599062378], [2, "DEF-123",1599062414], [1, "GHI-123",1599062435], [2, "GHI-123",1599062495], [1, "JKL-123",1599066000], [2, "JKL-123",1599066035]]))

# print(is_speeding([[2, "JKL-123",1599066035], [2, "ABC-123",1599066030], [1, "ABC-123",1599066000], [2, "DEF-123",1599062414], [1, "GHI-123",1599062435], [2, "GHI-123",1599062495], [1, "JKL-123",1599066000], [1, "DEF-123",1599062378]]))


# speed = Position2 - Position1 / time2 - Time1


# **** OOP POKER ****###
# use OOP to design a hand of poker
# classes: Card(name, value), Hand(5cards), Deck()
# outside of scope: Game(spread, players), chips/bets()

# class Card(suit, value):
#     """create a card"""

#     def __init__(self, suit, value):
#         self.suit = suit
#         self.value = value
#         if self.value == 1:
#             self.display_value = 'Ace'
#         elif self.value == 11:
#             self.display_value = 'Jack'
#         elif self.value == 12:
#             self.display_value = 'Queen'
#         elif self.value == 13:
#             self.display_value = 'King'
#         else:
#             self.display_value = value

#         self.display_name = f"{display_value} of {suit}s"

#     # !! decorator - called when it's needed only - display name would be a method called on this class when asked


# class Deck(type="standard"):
#     """create a deck of cards"""

#     def __init__(self, type):
#         self.type = type
#         self.cards = []
#         if self.type == "standard":
#             # add one of each combo of suit and value
#             for i in range(1, 14):
#                 # TODO: another loop here
#                 self.cards.append(Card('hearts', i))
#                 self.cards.append(Card('clubs', i))
#                 self.cards.append(Card('spades', i))
#                 self.cards.append(Card('diamonds', i))
        
#     # methods: shuffle(), deal(players)

#     def deal():
#         return self.cards.pop()


# class Hand(type="five-card draw"):
#     """create a hand of poker"""

#     def __init__(self, type):
#         self.type = type
#         self.cards = []
#         if self.type == "five-card draw"
#             i = 0
#             while i < 5:
#                 self.cards.append(this_game.deck.deal())
#                 i += 1
        
#     # methods: play a card, discard


# # how do you compare two hands
# # based on rankings and values

