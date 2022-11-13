from calculate_distance import calculate_distance


def find_nearest_neighbor(truck_destinations, current_location):
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
    if temp_distance == 1000:
        return 0, temp_loc
    else:
        return temp_distance, temp_loc


def distance_to_time(distance):
    return (distance / 18) * 60

