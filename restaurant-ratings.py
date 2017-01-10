# your code goes here
import sys

input_file = sys.argv[1]


def get_user_rating(ratings):
    """Prompts user for place and rating, updates dictionary"""

    new_place = raw_input("Name the restaurant: ")
    new_score = int(raw_input("Score of restaurant (0-5): "))
    ratings[new_place] = new_score
    return ratings


def get_user_choice(ratings):
    """ """

    print("1. View the current ratings list.")
    print("2. Add a new restaurant and rating.")
    print("3. Quit.")
    user_choice = raw_input(">>> ")

    if user_choice == "1":
        return ratings
    elif user_choice == "2":
        return get_user_rating(ratings)
    else:
        quit()


def rates_restaurants(file_name):
    """Returns alphabetized restaurant ratings"""

    data_file = open(file_name)

    ratings = {}
    for line in data_file:
        line = line.rstrip()
        restaurant, score = line.split(":")
        ratings[restaurant] = score

    data_file.close()

    ratings = get_user_choice(ratings)

    for place in sorted(ratings):
        print "{} is rated at {}.".format(place, ratings[place])


rates_restaurants(input_file)
