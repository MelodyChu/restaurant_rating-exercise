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
    print "1) See a sorted list of ratings \n2) Add new restaurant and rate it \nType 'q' to quit"
    user_choice = raw_input("What would you like to do? ")

    if user_choice == '1':
        for restaurant, ratings in sorted(restaurant_dict.items()):
            print '{} has a rating of {}'.format(restaurant, ratings)

    elif user_choice == '2':
        new_restaurant = raw_input("Enter name of restaurant: ")
   
        while True:
            try:
                new_rating = raw_input("\n How would you rate this restaurant from 1-5? ")
                if int(new_rating) in range(1, 6):
                    break
                print "Please provide a value between 1 and 5!"
            except ValueError:
                print "Invalid input. Please provide a value between 1 and 5!"
        restaurant_dict[new_restaurant] = new_rating

        for restaurant, ratings in sorted(restaurant_dict.items()):
            print '{} has a rating of {}'.format(restaurant, ratings)

    elif user_choice in 'Qq':
        print "Session terminated"
        return

    # else:



    # getting user input
    

    # sorting by the items
    # turns into tuples

input_restaurant("scores.txt")
