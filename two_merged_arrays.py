"Function that merges two sorted arrays"

def merge_sorted_arrays(array1, array2):
    if not array1:
        return array2
    if not array2:
        return array1
    result = []
    i = j = 0

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1
    result.extend(array1[i:])
    result.extend(array2[j:])
    return result

# recursion

def merge_sorted_arrays_recursion(array1, array2):
    if not array1:
        return array2
    if not array2:
        return array1
    
    if array1[0] <= array2[0]:
        return [array1[0]] + merge_sorted_arrays_recursion(array1[1:], array2)
    else:
        return [array2[0]] + merge_sorted_arrays_recursion(array1, array2[1:])