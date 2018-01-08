"""Restaurant rating lister."""


def get_ratings(filename):
    """Function which opens a .txt file and prints restaurant and corresponding
    rating.
    """
    ratings = open(filename)

    for line in ratings:
        rating_list = line.rstrip().split(":")
        # print rating_list
        restaurant, rating = rating_list
        print restaurant + " is rated " + rating

get_ratings("scores.txt")
