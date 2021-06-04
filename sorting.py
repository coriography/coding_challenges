def quick_sort(lst):
    # quicksort practice - codewars
    # time complexity - worst case: O(n^2); average case: O(nlogn)

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

print(quick_sort([3,6,1,3,2,8,4,8,3,8,3]))
print(quick_sort([3,6,-1,3,2,-8,4,8,3,8,-3]))
print(quick_sort([None]))
print(quick_sort([2]))
print(quick_sort([0]))
    