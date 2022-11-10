# C950 Task 1 -- David-Raphael Assouline 010251016
import datetime

from load_trucks import load_trucks, truck_one, truck_two, truck_three, truck_one_destinations
from nearest_neighbor import find_nearest_neighbor, distance_to_time

current_time = datetime.datetime(2022, 1, 1, 8, 0, 0)

load_trucks()
truck_one_next_destination = "195 W Oakland Ave"
counter = 1

while len(truck_one_destinations) > 1:
    print(f"Successfully delivered package to {truck_one_next_destination}")
    counter += 1
    print(counter)
    distance, destination = find_nearest_neighbor(truck_one_destinations, truck_one_next_destination)
    try:
        while True:
            truck_one_destinations.remove(truck_one_next_destination)
    except ValueError:
        pass
    truck_one_next_destination = destination
    current_time += datetime.timedelta(minutes=distance_to_time(distance))
    print(current_time)




