from search_functionality import search_city

def test_less_than_2_characters():
    assert search_city("s") == []

def test_more_than_2_characters():
    assert search_city("Va") == ["Valencia", "Vancouver"]

def test_case_issensitive():
    assert search_city("va") == ["Valencia", "Vancouver"]

def test_is_part_of_the_text():
    assert search_city("ape") == ["Budapest"]

def test_text_is_asterisk():
    assert search_city("*") == ["Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", 
        "Amsterdam", "Vienna", "Sydney", "New York City", "London", "Bangkok", 
        "Hong Kong", "Dubai", "Rome", "Istanbul"]