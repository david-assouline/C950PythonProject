# C950 Task 1 -- David-Raphael Assouline 010251016
import datetime
from load_trucks import load_trucks, truck_one_destinations, truck_two_destinations, truck_three_destinations, \
    truck_one, all_packages, truck_two, truck_three
from lookup_package import lookup_package
from nearest_neighbor import find_nearest_neighbor, distance_to_time
from print_report import generate_report

# initializes the departure time of truck 1 & 2 (November 11th at 8:00 A.M. and 8:30 A.M.)
truck_one_time = datetime.datetime(2022, 11, 11, 8, 0, 0)
truck_two_three_time = datetime.datetime(2022, 11, 11, 8, 45, 0)

# initializes the odometer at 0 miles
truck_one_total_distance = 0
truck_two_total_distance = 0
truck_three_total_distance = 0

# loads the 3 trucks with the packages they will deliver
load_trucks()

# initializes the first destination of each truck
truck_one_next_destination = "195 W Oakland Ave"
truck_two_next_destination = "233 Canyon Rd"
truck_three_next_destination = "2530 S 500 E"

# removes the destination of package #9 since it is a wrong address. The correct one will be added later
truck_three_destinations.remove("300 State St")
truck_three_new_address = False

# changes the status of all packages on truck 1 & 2 from "At Hub" to "En Route"
for i in all_packages.get_keys():
    if i in truck_one.get_keys() or i in truck_two.get_keys():
        all_packages.get_item(i)[-1] = "En Route"
truck_three_en_route = False

# main loop that runs until all packages are delivered
while True:
    # truck 1 will keep delivering its packages until it has no more destinations to go to
    if len(truck_one_destinations) > 0:
        packages_about_to_be_delivered = []
        # adds all the packages about to be delivered at given address into an array.
        for i in truck_one.get_keys():
            try:
                if truck_one.get_item(i) == truck_one_next_destination:
                    packages_about_to_be_delivered.append(i)
            except TypeError:
                pass
        # finds the nearest destination after the current one to deliver the next package
        # returns the distance to the next destination and the destination itself
        distance, destination = find_nearest_neighbor(truck_one_destinations, truck_one_next_destination)
        # adds the distance to the next destination to the odomoter of the current truck
        truck_one_total_distance += distance

        # removes the given destination from the list of destinations the truck must deliver to
        try:
            while True:
                truck_one_destinations.remove(truck_one_next_destination)
        except ValueError:
            pass

        # sets the truck's next destination
        truck_one_next_destination = destination

        # adds the elapsed time for the given delivery to the total timer for the given truck
        truck_one_time += datetime.timedelta(minutes=distance_to_time(distance))

        # changes the status of the given package from "En Route" to "Delivered" and logs the time of delivery
        for i in packages_about_to_be_delivered:
            all_packages.get_item(i)[-1] = f"Delivered at {truck_one_time}"
            all_packages.get_item(i)[-2] = truck_one_time

        # generates a report after each delivery of every package and its status, including each truck's
        # odometer, and prints it to console.
        generate_report(truck_one_total_distance, truck_two_total_distance, truck_three_total_distance, truck_one_time)

    if len(truck_two_destinations) > 0:
        packages_about_to_be_delivered = []
        for i in truck_two.get_keys():
            try:
                if truck_two.get_item(i) == truck_two_next_destination:
                    packages_about_to_be_delivered.append(i)
            except TypeError:
                pass
        distance, destination = find_nearest_neighbor(truck_two_destinations, truck_two_next_destination)
        truck_two_total_distance += distance
        try:
            while True:
                truck_two_destinations.remove(truck_two_next_destination)
        except ValueError:
            pass
        truck_two_next_destination = destination
        truck_two_three_time += datetime.timedelta(minutes=distance_to_time(distance))
        for i in packages_about_to_be_delivered:
            all_packages.get_item(i)[-1] = f"Delivered at {truck_two_three_time}"
            all_packages.get_item(i)[-2] = truck_two_three_time
        generate_report(truck_one_total_distance, truck_two_total_distance, truck_three_total_distance, truck_two_three_time)

    if len(truck_two_destinations) == 0 and len(truck_three_destinations) > 0:
        if not truck_three_en_route:
            print("*" * 20 + "Truck 3 leaving hub" + "*" * 20)
            for i in all_packages.get_keys():
                if i in truck_three.get_keys():
                    all_packages.get_item(i)[-1] = "En Route"
            truck_three_en_route = True
        if truck_two_three_time > datetime.datetime(2022, 11, 11, 10, 29, 59):
            if not truck_three_new_address:
                truck_three_destinations.append("410 S State St")
                truck_three_new_address = True
                all_packages.get_item("9")[0] = "410 S State St"
        packages_about_to_be_delivered = []
        for i in truck_three.get_keys():
            try:
                if truck_three.get_item(i) == truck_three_next_destination:
                    packages_about_to_be_delivered.append(i)
            except TypeError:
                pass
        distance, destination = find_nearest_neighbor(truck_three_destinations, truck_three_next_destination)
        truck_three_total_distance += distance
        try:
            while True:
                truck_three_destinations.remove(truck_three_next_destination)
        except ValueError:
            pass
        truck_three_next_destination = destination
        truck_two_three_time += datetime.timedelta(minutes=distance_to_time(distance))
        for i in packages_about_to_be_delivered:
            all_packages.get_item(i)[-1] = f"Delivered at {truck_two_three_time}"
            all_packages.get_item(i)[-2] = truck_two_three_time
        generate_report(truck_one_total_distance, truck_two_total_distance, truck_three_total_distance,
                        truck_two_three_time)
    if len(truck_three_destinations) == 0:
        print("Welcome to the WGUPS interface! Please select an option:")
        while True:
            user_selection = input("Enter 1 to lookup a package\nEnter 2 to exit this application\n")
            if user_selection == "2":
                exit(1)
            elif user_selection == "1":
                package_number = input("What is the Package ID?\n")
                package_hour = input("What is the lookup hour (0-23)?\n")
                package_minute = input("What is the lookup minute (0-59)?\n")
                lookup_package(package_number, datetime.datetime(2022, 11, 11, int(package_hour), int(package_minute)))
                print("*" * 40)
            else:
                print("Input not recognized. Please try again")

