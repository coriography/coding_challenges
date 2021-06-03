# *** twoSum problem

# twoSum([6, 5, 3, 4, 1, 2], 7); // [ 2, 3 ]

# return indices of two integers that add to target int

# iterate over list 
# see if current int subtracted from target equals any other int
# (requires nested loop)

# def twoSum(list_int, target):
#     for i in list_int:
#         print (i)

# twoSum([1, 8, 3, 4], 9)

# **** Linked Lists practice **** #

# class Node():
#     """creates a Node class."""

#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList():
#     """creates a Singly-Linked List class."""

#     def __init__(self):
#         self.head = None

#     def list_print(self):
#         """prints list of all nodes' data."""

#         current = self.head

#         while current:
#             print(current.data)
#             current = current.next

#     def insert_head(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def insert_tail(self, new_data):
#         new_node = Node(new_data)
#         current = self.head

#         while current.next:
#             current = current.next
        
#         current.next = new_node
#         new_node.next = None

#     def insert_after(self, p_data, new_data):
#         new_node = Node(new_data)
#         current = self.head

#         while current:
#             if current.data == p_data:
#                 new_node.next = current.next
#                 current.next = new_node
#                 return catlist.list_print()
#             else:
#                 current = current.next

#     def remove_node(self, remove_data):
#         prev = None
#         current = self.head

#         while current:
#             if current.data == remove_data:
#                 if prev:
#                     prev.next = current.next
#                 else:
#                     self.head = current.next
#                 return print("removed data")

#             prev = current
#             current = current.next

#         return print("data not in list")
            

# node1 = Node('Tuna')
# node2 = Node('Guppy')
# node3 = Node('Loja')
# catlist = LinkedList()
# catlist.head = node1
# catlist.head.next = node2
# node2.next = node3
# catlist.insert_head('Catsper')
# catlist.insert_tail('Sammy')
# catlist.insert_after('Tuna', 'Turner')


# **** Lee interview q ****###
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




########*#########
##* RECURSION *###
########*#########

# TODO: change loops to recursive

# def count_loop():
#     """Count to 3, using a while loop."""

#     n = 1

#     while n <= 3:
#         print(n)
#         n = n + 1

# count_loop()

# def r_count_loop(n=1):
#     """Count to 3 using a recursive call."""

#     # base case
#     if n == 3:
#         return print(n)

#     print(n)
#     r_count_loop(n=n+1)

# r_count_loop()

# def lst_len(my_list):
#     """Return length of list using recursion without using len()"""

#     if not my_list:
#         return 0
    
#     return 1 + lst_len(my_list[1:])


# print(lst_len([3,6,2,7]))


###########*############
##* STACKS & QUEUES *###
###########*############

 