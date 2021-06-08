
###** NON-CONSTRUCTIBLE CHANGE **###

# given an array of positive int representing the value of non-unique coins in your pocket, write a function that returns the minimum amount of change you cannot create.


def find_min_change(pocket_change):
    """finds minimum change possible from given pocket change.
    >>> (find_min_change([1,2,5]))
    4
    >>> (find_min_change([5,7,1,1,2,3,22]))
    20
    """

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

