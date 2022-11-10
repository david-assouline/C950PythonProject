from datetime import datetime

from pandas import read_csv

from calculate_distance import calculate_distance


def find_nearest_neighbor(truck_destinations, current_location):
    data = read_csv("data/distance_name_data.csv")
    temp_distance = 1000
    temp_loc = None
    for potential_location in truck_destinations:
        current_distance = calculate_distance(current_location, potential_location)
        if current_distance == None:
            pass
        elif current_distance < temp_distance:
            temp_distance = current_distance
            temp_loc = potential_location
        else:
            pass
    return temp_distance, temp_loc


def distance_to_time(distance):
    return (distance / 18) * 60

