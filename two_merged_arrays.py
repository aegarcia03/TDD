"Function that merges two sorted arrays"

def merge_sorted_arrays(array1, array2):
    if not array1:
        return array2
    if not array2:
        return array1
    return []