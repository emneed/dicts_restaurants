# your code goes here
import sys

input_file = sys.argv[1]


def rates_restaurants(file_name):
    """Returns alphabetized restaurant ratings"""

    data_file = open(file_name)

    ratings = {}
    for line in data_file:
        line = line.rstrip()
        restaurant, score = line.split(":")
        ratings[restaurant] = score

    data_file.close()

    for place in sorted(ratings):
        print "{} is rated at {}.".format(place, ratings[place])

rates_restaurants(input_file)
