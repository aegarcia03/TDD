from two_merged_arrays import merge_sorted_arrays

def test_empty_arrays():
    assert merge_sorted_arrays([],[]) == []

def test_one_empty_array():
    assert merge_sorted_arrays([],[1,2,3]) == [1,2,3]
    assert merge_sorted_arrays([2,5,6],[]) == [2,5,6]