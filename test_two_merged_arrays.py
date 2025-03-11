from two_merged_arrays import merge_sorted_arrays
from two_merged_arrays import merge_sorted_arrays_recursion

def test_empty_arrays():
    assert merge_sorted_arrays([],[]) == []

def test_one_empty_array():
    # When one array is empty, should return the other array
    assert merge_sorted_arrays([],[1,2,3]) == [1,2,3]
    assert merge_sorted_arrays([2,5,6],[]) == [2,5,6]

def test_non_overlapping_arrays():
    #When arrays do not overlap, should merge in order
    assert merge_sorted_arrays([1,4,5],[6,7,8]) == [1,4,5,6,7,8]
    assert merge_sorted_arrays([6,7,8],[1,2,2]) == [1,2,2,6,7,8]
    assert merge_sorted_arrays_recursion([6,7,8],[1,2,2]) == [1,2,2,6,7,8]

def test_overlapping_arrays():
    assert merge_sorted_arrays([1,3,5,7],[3,4,7,8]) == [1,3,3,4,5,7,7,8]
    assert merge_sorted_arrays_recursion([1,3,5,7],[3,4,7,8]) == [1,3,3,4,5,7,7,8]


def tes_negative_numbers():
    assert merge_sorted_arrays_recursion([-1,-3,-5,7],[-3,-4,-7,-8]) == [-8,-7,-5,-4,-3,-3,-1,7]