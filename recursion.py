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
