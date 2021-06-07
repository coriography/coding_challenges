def quick_sort(lst):
    # time complexity - worst case: O(n^2); average case: O(nlogn)
    # general idea: choose a pivot or partition and move items higher or lower then pivot.
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

def merge_sort(lst):
    # time complexity - worst case: O(nlogn); average case: O(nlogn)
    # make_one_sorted_list × number_of_levels = O(n) * O(log n) → O(n log n)
    # general idea: reduce lists to 0-1 el
    # recombine by comparint first el of each list and putting lower one first

    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = new_index = 0

        # combine left and right into list

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                lst[new_index] = left[left_index]
                left_index += 1
            else:
                lst[new_index] = right[right_index]
                right_index += 1
            new_index += 1

        # If lists were uneven length, add remainder of longer list

        while left_index < len(left):
            lst[new_index] = left[left_index]
            left_index += 1
            new_index += 1

        while right_index < len(right):
            lst[new_index] = right[right_index]
            right_index += 1
            new_index += 1

    return lst

print(merge_sort([3,6,-1,3,2,-8,4,8,3,8,-3]))
print(merge_sort([3,6,1,3,2,8,4,8,3,8,3]))
print(merge_sort([None]))
print(merge_sort([2]))
print(merge_sort([0]))
