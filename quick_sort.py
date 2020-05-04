"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    # print "top of call"
    # print array
    if len(array) <= 1:
        return array
    if len(array) == 2:
        return [min(array), max(array)]
    pivot = array[-1]
    pivot_index = len(array) - 1
    position_to_check = 0
    while position_to_check < pivot_index:
        # print "top of check"
        # print array
        # print "pivot index: {}, position_to_check: {}".format(pivot_index, position_to_check)
        if array[position_to_check] <= pivot:
            position_to_check += 1
        else:
            el = array.pop(position_to_check) 
            array.append(el)
            pivot_index -= 1
            # array.insert(0, array.pop(pivot_index - 1))
            position_to_check = 0
            # print "numbers shifted:"
            # print array

    # print "Halves: "
    # print pivot_index
    # print (array[:pivot_index])
    # print (array[pivot_index:])
    return quicksort(array[:pivot_index]) + quicksort(array[pivot_index:])

test = [22, 4, 1, 5, 7, 0, -2, 11, 1221]
test = []
test = [23]
# test = [1, 1, 1]
test = [1, 2, 3, 4, 5, 4, 4, 3, 0]
print quicksort(test) == sorted(test)

