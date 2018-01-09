def input_restaurant(filename):
    """Takes input from user about restaurant and rating and prints the
    the original list and the new addition
    """

    file1 = open(filename)
    #restaurant_list = file1.split(':')
    restaurant_dict = {}

    #for item in restaurant_list:
    for line in file1:
        restaurant_list = line.rstrip().split(':')
        restaurant, rating = restaurant_list
        restaurant_dict[restaurant] = rating
    # print restaurant_dict

    # getting user input
    new_restaurant = raw_input("Enter name of restaurant: ")
    new_rating = raw_input("How would you rate this restaurant from 1-5? ")

    restaurant_dict[new_restaurant] = new_rating
    # sorting by the items
    # turns into tuples
    for restaurant, ratings in sorted(restaurant_dict.items()):
        print '{} has a rating of {}'.format(restaurant, ratings)

input_restaurant("scores.txt")
