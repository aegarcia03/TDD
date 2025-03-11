# '''The function takes a string (search text) as input and 
# returns the found cities which corresponds to the search text.'''

# def search_city(text):
#     city_names = [
#         "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", 
#         "Amsterdam", "Vienna", "Sydney", "New York City", "London", "Bangkok", 
#         "Hong Kong", "Dubai", "Rome", "Istanbul"
#     ]

#     if len(text) < 2:
#         return []
    
#     matching_cities = []
#     for city in city_names:
#         if city.lower().startswith(text.lower()):
#             matching_cities.append(city)


#     return matching_cities

# Refactor

# def search_city(text):
#     city_names = [
#         "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", 
#         "Amsterdam", "Vienna", "Sydney", "New York City", "London", "Bangkok", 
#         "Hong Kong", "Dubai", "Rome", "Istanbul"
#     ]

#     if text == "*":
#         return city_names

#     if len(text) < 2:
#         return []

    
#     matching_cities = []
#     for city in city_names:
#         if text.lower() in city.lower():
#             matching_cities.append(city)

#     return matching_cities

#Refactor
def search_city(text):
    city_names = [
        "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver", 
        "Amsterdam", "Vienna", "Sydney", "New York City", "London", "Bangkok", 
        "Hong Kong", "Dubai", "Rome", "Istanbul"
    ]

    if text == "*":
        return city_names

    if len(text) < 2:
        return []

    
    return [city for city in city_names if text.lower() in city.lower()]
