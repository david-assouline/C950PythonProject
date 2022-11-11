# C950 Task 1 -- David-Raphael Assouline 010251016
import datetime
from load_trucks import load_trucks, truck_one_destinations, truck_two_destinations, truck_three_destinations, \
    truck_one, all_packages, truck_two
from nearest_neighbor import find_nearest_neighbor, distance_to_time
from print_report import generate_report

truck_one_time = datetime.datetime(2022, 1, 1, 8, 0, 0)
truck_two_three_time = datetime.datetime(2022, 1, 1, 8, 0, 0)
truck_one_total_distance = 0
truck_two_total_distance = 0
truck_three_total_distance = 0

load_trucks()
truck_one_next_destination = "195 W Oakland Ave"
truck_two_next_destination = "233 Canyon Rd"
truck_three_next_destination = "2530 S 500 E"

for i in all_packages.get_keys():
    if i in truck_one.get_keys() or i in truck_two.get_keys():
        all_packages.get_item(i)[-1] = "En Route"

while True:
    if len(truck_one_destinations) > 1:
        packages_about_to_be_delivered = []
        for i in truck_one.get_keys():
            try:
                if truck_one.get_item(i) == truck_one_next_destination:
                    packages_about_to_be_delivered.append(i)
            except TypeError:
                pass
        #print(f"Successfully delivered package(s) {packages_about_to_be_delivered} from truck #1 to {truck_one_next_destination}")
        distance, destination = find_nearest_neighbor(truck_one_destinations, truck_one_next_destination)
        truck_one_total_distance += distance
        try:
            while True:
                truck_one_destinations.remove(truck_one_next_destination)
        except ValueError:
            pass
        truck_one_next_destination = destination
        truck_one_time += datetime.timedelta(minutes=distance_to_time(distance))
        for i in packages_about_to_be_delivered:
            all_packages.get_item(i)[-1] = f"Delivered at {truck_one_time}"
        generate_report(truck_one_total_distance, truck_two_total_distance, truck_three_total_distance, truck_one_time)

    if len(truck_two_destinations) > 1:
        print(f"Successfully delivered package from truck #2 to {truck_two_next_destination}")
        distance, destination = find_nearest_neighbor(truck_two_destinations, truck_two_next_destination)
        truck_two_total_distance += distance
        try:
            while True:
                truck_two_destinations.remove(truck_two_next_destination)
        except ValueError:
            pass
        truck_two_next_destination = destination
        truck_two_three_time += datetime.timedelta(minutes=distance_to_time(distance))
        print(truck_two_three_time)
        print(F"Truck 2 total distance: {round(truck_two_total_distance, 2)} miles")

    if len(truck_two_destinations) == 1 and len(truck_three_destinations) > 1:
        print(f"Successfully delivered package from truck #3 to {truck_three_next_destination}")
        distance, destination = find_nearest_neighbor(truck_three_destinations, truck_three_next_destination)
        truck_three_total_distance += distance
        try:
            while True:
                truck_three_destinations.remove(truck_three_next_destination)
        except ValueError:
            pass
        truck_three_next_destination = destination
        truck_two_three_time += datetime.timedelta(minutes=distance_to_time(distance))
        print(truck_two_three_time)
        print(F"Truck 3 total distance: {round(truck_three_total_distance, 2)} miles")

for i in range(39):
    if str(i) in truck_one.get_keys():
        print("true")