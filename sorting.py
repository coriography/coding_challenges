def quick_sort(lst):
    # time complexity - worst case: O(n^2); average case: O(nlogn)
    # general idea: choose a pivot and move items higher or lower then pivot.
    # repeat with each half of the list and so on.

    # ** option 1: Hackbright solution ** #

    # if lst == None or len(lst) == 0:
    #     return []
    
    # import random

    # def _quicksort(lst, first, last):
    #     if first < last:

    #         # Find pivot point

    #         pivot = first + random.randrange(last - first + 1)
    #         lst[pivot], lst[last] = lst[last], lst[pivot]

    #         pivot = first

    #         for i in range(pivot, last):
    #             if lst[i] <= lst[last]:
    #                 lst[i], lst[pivot] = lst[pivot], lst[i]
    #                 pivot += 1

    #         lst[pivot], lst[last] = lst[last], lst[pivot]

    #         # Recurse
    #         _quicksort(lst, first, pivot - 1)
    #         _quicksort(lst, pivot + 1, last)

    # _quicksort(lst, 0, len(lst) - 1)
    
    # return lst

    # ** option 2: "buckets" solution ** #
    # simpler solution, worse time & space complexity

    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()
        lo = []
        hi = []

    for el in lst:
        if el <= pivot:
            lo.append(el)
        else:
            hi.append(el)

    return quick_sort(lo) + [pivot] + quick_sort(hi)

# print(quick_sort([3,6,1,3,2,8,4,8,3,8,3]))
# print(quick_sort([3,6,-1,3,2,-8,4,8,3,8,-3]))
# print(quick_sort([None]))
# print(quick_sort([2]))
# print(quick_sort([0]))
    

def bubble_sort(lst):

    # time complexity - worst case: O(n^2); average case: O(nlogn)
    # general idea: moving through list, compare two adjacent elements
    # if 1st is greater than 2nd, swap them
    # continue until list is sorted

    if len(lst) <= 1:
        return lst

    for i in range(0, len(lst) - 1):
        made_swap = False # keeps track of whether swap is made first time through
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                made_swap = True

        if not made_swap: # nothing was swapped, so we can return
            return lst

    return lst

# print(bubble_sort([3,6,-1,3,2,-8,4,8,3,8,-3]))
# print(bubble_sort([3,6,1,3,2,8,4,8,3,8,3]))
# print(bubble_sort([None]))
# print(bubble_sort([2]))
# print(bubble_sort([0]))

def selection_sort(lst):
    # time complexity - worst case: O(n^2); average case: O(n^2)
    # general idea:

    pass

def insertion_sort(lst):
    # time complexity - worst case: O(n^2); average case: O(n^2)
    # general idea:

    pass