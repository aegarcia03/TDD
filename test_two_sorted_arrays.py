from two_sorted_arrays import two_sorted_arrays

def test_two_sorted_arrays():
    assert two_sorted_arrays([],[]) == []
    
def test_one_empty_array_other_non_empty():
    assert two_sorted_arrays([],[1,2,3]) == [1,2,3]

def test_one_non_empty_other():
    assert two_sorted_arrays([1,2,3],[]) == [1,2,3]
  
def test_two_non_overlapping():
    assert two_sorted_arrays([1,2,3],[4,5,6]) == [1,2,3,4,5,6]
    assert two_sorted_arrays([4,5,6],[1,2,3]) == [1,2,3,4,5,6]

def test_one_with_duplicates():
    assert two_sorted_arrays([5,6,7],[1,2,2]) == [5,6,7,1,2,2]
                                              