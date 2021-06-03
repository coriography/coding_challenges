def solution(lst):
    # quicksort practice - codewars

    if lst == None or len(lst) == 0:
        return []
    
    import random

    def _quicksort(lst, first, last):
        if first < last:

            # Find pivot point

            pivot = first + random.randrange(last - first + 1)
            lst[pivot], lst[last] = lst[last], lst[pivot]

            pivot = first

            for i in range(pivot, last):
                if lst[i] <= lst[last]:
                    lst[i], lst[pivot] = lst[pivot], lst[i]
                    pivot += 1

            lst[pivot], lst[last] = lst[last], lst[pivot]

            # Recurse
            _quicksort(lst, first, pivot - 1)
            _quicksort(lst, pivot + 1, last)

    _quicksort(lst, 0, len(lst) - 1)
    
    return lst